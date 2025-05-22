# git_utils.py
import subprocess

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {cmd}\nError: {result.stderr}")
    return result.stdout.strip()

def get_git_diff():
    return run("git diff")

def create_branch(branch_name):
    run(f"git checkout -b {branch_name}")

def add_commit_push(commit_message, branch_name):
    run("git add .")
    run(f'git commit -m "{commit_message}"')
    run(f"git push origin {branch_name}")

def create_pr(title, body, base, head):
    # Requires `gh` CLI installed and authenticated
    pr_cmd = f'gh pr create --title "{title}" --body "{body}" --base {base} --head {head}'
    output = run(pr_cmd)
    return output