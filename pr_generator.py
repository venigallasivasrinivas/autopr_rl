# pr_generator.py

import subprocess

def generate_pr_text(diff_text, model="llama2"):
    prompt = (
        "Summarize the following git diff into a concise PR title and detailed description:\n\n"
        f"{diff_text}\n\n"
        "PR Title:\nPR Description:"
    )
    try:
        result = subprocess.check_output(['ollama', 'run', model], input=prompt.encode())
        return result.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError("Ollama call failed") from e