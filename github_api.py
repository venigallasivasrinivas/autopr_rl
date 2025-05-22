# github_api.py

from github import Github
import os

def create_pull_request(token, repo_name, title, body, head_branch, base_branch):
    g = Github(token)
    repo = g.get_repo(repo_name)
    pr = repo.create_pull(title=title, body=body, head=head_branch, base=base_branch)
    return pr.number, pr.html_url