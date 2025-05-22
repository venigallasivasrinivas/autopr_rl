✅ README Update Suggestions

🔹 Project Overview

Briefly describe what the project does, e.g.:

Automatically generates PR titles and descriptions using a local Ollama LLaMA model and git diffs.

🔹 Installation

git clone https://github.com/your-username/autopr_rl.git
cd autopr_rl
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

🔹 Ollama Setup

Make sure Ollama is installed and the desired model is pulled:

ollama run llama2

🔹 Usage

python main.py

This will:
	•	Fetch the current git diff
	•	Send it to the Ollama LLaMA model via llama_generator.py
	•	Generate a draft PR title and description
	•	(Optionally) Commit and push the changes

🔹 File Descriptions
	•	main.py: Entry point for the PR generator
	•	llama_generator.py: Uses Ollama API to generate PR content
	•	llama_improver.py: Optionally refines the PR content
	•	utils.py: Git diff utilities

🔹 Configurable Settings

If applicable, describe things like:
	•	Default model (llama2, mistral, etc.)
	•	Git branch creation
	•	Prompt templates

🔹 Example

# Sample output
Title: Refactor PR generator to use streaming model response

Description:
- Switched to streaming API for faster response time
- Handled JSON decode errors gracefully
- Updated model to `llama2` for better local inference