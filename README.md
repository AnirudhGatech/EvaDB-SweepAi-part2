# EvaDB-SweepAI-2

This prototype performs several tasks such as setting up a PostgreSQL database, interacting with the OpenAI API for code corrections, optimizing queries in the database, and automating GitHub commits with corrected code snippets.


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

3. Set up PostgreSQL and create a database named `evadb`.

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

