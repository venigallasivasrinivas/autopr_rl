# gh_diff.py

import subprocess

def get_git_diff(path="."):
    """Get the output of git diff in the given path."""
    try:
        diff = subprocess.check_output(['git', '-C', path, 'diff']).decode('utf-8')
        if not diff.strip():
            raise ValueError("No git changes found.")
        return diff
    except subprocess.CalledProcessError:
        raise RuntimeError("Not a git repository or error in fetching diff.")