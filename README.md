# EvaDB-SweepAI-2

This prototype performs several tasks such as setting up a PostgreSQL database, interacting with the OpenAI API for code corrections, optimizing queries in the database, and automating GitHub commits with corrected code snippets. 
This prototype performs several tasks:

1. **PostgreSQL Setup and Database Configuration:**
   - Installs PostgreSQL and starts the service.
   - Creates a PostgreSQL user and database for use in the code.

2. **Package Installation:**
   - Installs necessary Python packages (`evadb` and `psycopg2`).

3. **Database Table Creation:**
   - Creates tables (`code_embeddings_table`, `response`, `issue_table`) within the PostgreSQL database (`evadb`).

4. **OpenAI API Integration:**
   - Sets up the OpenAI API key for use in generating code embeddings.

5. **Code Preprocessing and Embedding:**
   - Defines functions to preprocess Python code by removing comments and single quotes.
   - Implements a function to generate embeddings of code snippets using OpenAI's API.

6. **Database Operations:**
   - Inserts code embeddings into the PostgreSQL database in batches.
   - Creates indexes on the database tables (`code_embeddings_table`) to optimize queries.

7. **GitHub Interaction and Automation:**
   - Clones a specified GitHub repository locally.
   - Modifies files in the cloned repository with corrected code snippets obtained from the ChatGPT model.
   - Stages, commits, and pushes changes to the GitHub repository using Git commands.
   - Cleans up the cloned repository directory after the commit is pushed.

These tasks collectively set up the database, process code snippets, optimize database operations, interact with the GitHub API, and automate the correction and commit of code snippets within a specified repository.

## Setup

### Requirements

- Python 3.6 or higher
- PostgreSQL
- OpenAI API key

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/code-automation-tool.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure PostgreSQL by establishing a database named 'evadb.' The script within this repository presupposes the utilization of a PostgreSQL database. To employ alternative databases, adjustments might be necessary in the section connecting the database with the 'evadb' library.

 4. Export the OpenAI API key as an environment variable:

    ```bash
    export OPENAI_KEY=your_openai_api_key_here
    ```

## Usage

1. Update the repository owner and repository name variables (`repo_owner` and `repo_name`) in the code with your GitHub repository details.

2. Run the script:

    ```bash
    python code_automation.py
    ```

3. The tool will clone the specified GitHub repository, fetch code snippets, correct them using the OpenAI GPT model, and create a commit with the corrected code.



#### Input:

1. **GitHub Repository Information**:
   - **Repository Owner**: Replace_with_Repository_Owner
   - **Repository Name**: Replace_with_Repository_Name

2. **Python Code Snippets from GitHub**:
   - Python code files present in the specified repository. For instance:
     - `file1.py`
     - `file2.py`
   - These files contain Python code with potential issues or problems that need correction.




#### Output:

1. **Updated Python Code Files**:
   - `issue-1.py`, `issue-2.py`, etc. (if issues are detected and corrected).
   - These files contain corrected code snippets based on the ChatGPT suggestions for identified issues.

2. **GitHub Interaction Logs**:
   - Logs and messages indicating successful cloning, code analysis, correction, commit creation, and push to the repository.

