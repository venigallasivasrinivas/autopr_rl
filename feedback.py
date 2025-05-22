# feedback.py

def get_pr_feedback(repo, pr_number):
    pr = repo.get_pull(pr_number)
    reviews = pr.get_reviews()
    is_merged = pr.is_merged()
    return {
        "merged": is_merged,
        "review_comments": [r.body for r in reviews]
    }