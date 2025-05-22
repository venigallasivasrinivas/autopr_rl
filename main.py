# main.py
import os
import time
from dotenv import load_dotenv
from git_utils import get_git_diff, create_branch, add_commit_push, create_pr
from llama_generator import generate_pr_text
load_dotenv()

def main():
    repo_name = os.getenv("REPO_NAME")
    base_branch = os.getenv("BASE_BRANCH", "main")
    head_branch = f"feature-branch-{int(time.time())}"

    # Step 1: get current git diff
    diff_text = get_git_diff()
    if not diff_text.strip():
        print("No changes detected. Exiting.")
        return

    # Step 2: generate PR title and body using LLaMA (or dummy)
    title, body = generate_pr_text(diff_text)
    print(f"Generated PR Title:\n{title}")
    print(f"Generated PR Body:\n{body}\n")

    # Step 3: Create new git branch, commit changes, push
    try:
        create_branch(head_branch)
    except Exception as e:
        print(f"Warning: Could not create branch (may already exist): {e}")

    try:
        add_commit_push(body, head_branch)
    except Exception as e:
        print(f"Failed to add, commit, or push changes: {e}")
        return

    # Step 4: Create pull request with gh CLI
    try:
        output = create_pr(title, body, base_branch, head_branch)
        print(f"Pull request created:\n{output}")
    except Exception as e:
        print(f"Failed to create PR: {e}")

if __name__ == "__main__":
    main()