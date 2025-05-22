# main.py

import os
from dotenv import load_dotenv
from gh_diff import get_git_diff
from pr_generator import generate_pr_text
from github_api import create_pull_request
from github import Github

def main():
    load_dotenv()
    diff = get_git_diff()
    pr_text = generate_pr_text(diff)

    print("\n=== Generated PR ===\n")
    print(pr_text)

    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("REPO_NAME")
    head_branch = os.getenv("HEAD_BRANCH", "feature-branch")
    base_branch = os.getenv("BASE_BRANCH", "main")

    title, body = pr_text.split('\n', 1)
    pr_number, url = create_pull_request(token, repo_name, title, body, head_branch, base_branch)
    print(f"\nPull Request created: {url} (#{pr_number})")

if __name__ == "__main__":
    main()