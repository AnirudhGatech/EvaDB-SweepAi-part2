# EvaDB-SweepAI-2




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


