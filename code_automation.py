import re
import pandas as pd
import evadb
import os
import openai
import tokenize
import io
import github
import numpy as np
import warnings
from evadb.configuration.constants import EvaDB_INSTALLATION_DIR
import requests
import base64
import time

# Set up PostgreSQL
!apt install postgresql
!service postgresql start
!sudo -u postgres psql -c "CREATE USER yd WITH SUPERUSER PASSWORD 'gatech'"
!sudo -u postgres psql -c "CREATE DATABASE evadb"

# Install required packages
%pip install --quiet "evadb[document]"
%pip install psycopg2

# Connect to PostgreSQL
params = {
    "user": "user1  ",
    "password": "password",
    "host": "localhost",
    "port": "5432",
    "database": "evadb",
}
    
evadb_cursor = evadb.connect().cursor()
query = f"CREATE DATABASE postgres_data WITH ENGINE = 'postgres', PARAMETERS = {params};"
evadb_cursor.query(query).df()

# Create necessary tables
evadb_cursor.query("""
    USE postgres_data {
        DROP TABLE IF EXISTS code_embeddings_table;
        DROP TABLE IF EXISTS response;
        DROP TABLE IF EXISTS issue_table;
    }
""").df()

     
evadb_cursor.query("""
    USE postgres_data {
        CREATE TABLE code_embeddings_table (code_snippet TEXT(100), embedding NDARRAY FLOAT32(1,1536));
        CREATE TABLE response (response TEXT(200));
        CREATE TABLE issue_table (name VARCHAR(10), issue VARCHAR(1000));
    }
""").df()

# OpenAI API key setup
os.environ["OPENAI_KEY"] = "your_openai_api_key_here"
openai.api_key = os.environ["OPENAI_KEY"]

# Function to get tokens
def get_tokens(code):
    tokens = []
    for tok in tokenize.tokenize(io.BytesIO(code.encode('utf-8')).readline):
        tokens.append(tok.string)
    return ' '.join(tokens)

# Preprocess Python code
def preprocess_python_code(code):
    
    code = re.sub(r'#.*?\n', '\n', code)
    code = re.sub(r"'''(.*?)'''", '', code, flags=re.DOTALL)  
    code = re.sub(r'"""(.*?)"""', '', code, flags=re.DOTALL) 

   
    code = code.replace("'", "")
    return code.strip()

# Generate embeddings with OpenAI
def get_code_embedding(code: str) -> list:
    tokenized_code = get_tokens(code)
    response = openai.Embedding.create(input=tokenized_code, model="text-embedding-ada-002")
    embedding = response['data'][0]['embedding']
    embedding = np.array(embedding).reshape(1,-1)
    return embedding

# Insert code embedding into the database (batch insert)
def insert_code_embeddings(code_snippets):
    embeddings = []
    for code_snippet in code_snippets:
        embedding = get_code_embedding(code_snippet).tolist()
        embeddings.append((code_snippet, embedding))
    
    evadb_cursor.query(f"""
        USE postgres_data {{
            INSERT INTO code_embeddings_table (code_snippet, embedding)
            VALUES %s;
        }}
    """, params=embeddings).df()

# Create Indexes in the database for optimization
evadb_cursor.query("""
    USE postgres_data {
        CREATE INDEX IF NOT EXISTS code_snippet_index
        ON code_embeddings_table (code_snippet);
    }
""").df()

evadb_cursor.query("""
    USE postgres_data {
        CREATE INDEX IF NOT EXISTS code_embedding_index
        ON code_embeddings_table (STR2ARRAY(embedding))
        USING FAISS;
    }
""").df()

# Automation of  GitHub Commit Process
def automate_github_commit(repo_owner, repo_name):
    # Clone the repository locally
    os.system(f"git clone https://github.com/{repo_owner}/{repo_name}.git")
    os.chdir(repo_name)

    
    # Modify files with corrected code snippets
    for index in range(1, 3):  # Assuming issue-1.py and issue-2.py were generated
        issue_file = f"issue-{index}.py"
        if os.path.exists(issue_file):
            with open(issue_file, "r") as file:
                corrected_code = file.read()
                # Replace the content of respective files in the repository with corrected code
                with open(f"file{index}.py", "w") as repo_file:
                    repo_file.write(corrected_code)

    # Stage changes
    os.system("git add .")

    # Commit changes
    commit_message = "Automated correction of code issues"
    os.system(f'git commit -m "{commit_message}"')

    # Push changes to GitHub
    os.system("git push origin master")

    # Clean up cloned repository directory
    os.chdir("..")
    os.system(f"rm -rf {repo_name}")

# Specify the GitHub repository details for automation
repo_owner = "your_github_username"
repo_name = "your_repository_name"

# Perform GitHub commit automation
automate_github_commit(repo_owner, repo_name)

