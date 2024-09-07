import os
from github import Github

# Path to GitHub token and commit file within the repo directory
base_dir = os.path.dirname(__file__)
repo_dir = os.path.abspath(os.path.join(base_dir, '..'))  # Assuming the repo is one level up from the script
token_file_path = os.path.join(repo_dir, 'otherfiles', 'github_token.txt')
commit_file = os.path.join(repo_dir, 'otherfiles', 'last_commit.txt')

# Load GitHub token from the token file
try:
    with open(token_file_path, 'r') as token_file:
        GITHUB_TOKEN = token_file.read().strip()
except FileNotFoundError:
    print(f"Token file not found at {token_file_path}")
    exit(1)

# Initialize GitHub API using the secure token
g = Github(GITHUB_TOKEN)

# GitHub repository details
REPO_NAME = "Ram495-ctrl/CICD_HV"

def get_latest_commit(repo_name):
    try:
        repo = g.get_repo(repo_name)
        commits = repo.get_commits()
        latest_commit = commits[0].sha
        return latest_commit
    except Exception as e:
        print(f"Error retrieving commits: {e}")
        exit(1)

def read_last_commit():
    if os.path.exists(commit_file):
        try:
            with open(commit_file, 'r') as file:
                return file.read().strip()
        except IOError as e:
            print(f"Error reading commit file: {e}")
            exit(1)
    return None

def write_last_commit(commit):
    try:
        with open(commit_file, 'w') as file:
            file.write(commit)
    except IOError as e:
        print(f"Error writing commit file: {e}")
        exit(1)

# Main script execution
if __name__ == "__main__":
    latest_commit = get_latest_commit(REPO_NAME)
    last_commit = read_last_commit()

    if latest_commit != last_commit:
        print(f"New commit detected: {latest_commit}")
        write_last_commit(latest_commit)
    else:
        print("No new commits.")

