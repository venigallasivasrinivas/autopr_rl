🚀 AutoPR-RL: AI-powered Pull Request Title & Description Generator ✍️🤖

AutoPR-RL is a handy tool that helps developers write better pull request (PR) titles and descriptions automatically.
It reads the changes in your code (git diff) and uses a local AI model (LLaMA 2 via Ollama) to generate clear, meaningful PR text. ✨

⸻

🤔 What does it do?
	•	🔍 Looks at the difference between your current code and the last commit (git diff)
	•	🧠 Sends this info to a local AI model running on your machine (via Ollama)
	•	✍️ The AI writes a draft PR title and description for you
	•	⏳ Saves you time and makes your PRs easier to understand for reviewers

⸻

🛠️ How to Set It Up

1. 📥 Clone this repository

Open your terminal and run:

git clone https://github.com/venigallasivasrinivas/autopr_rl.git
cd autopr_rl

2. 🐍 Create and activate a Python virtual environment

This keeps dependencies separate from your system Python.

python3 -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate.bat      # On Windows

3. 📦 Install required Python packages

pip install --upgrade pip
pip install -r requirements.txt

(Make sure you have requests and other packages listed in requirements.txt)

4. 🤖 Make sure you have Ollama installed and running locally
	•	Download and install Ollama from https://ollama.com/
	•	Run the Ollama server and make sure your LLaMA 2 model is ready to receive requests.

5. ▶️ Run the tool

python main.py

The tool will read your current git diff and generate a suggested PR title and description.

⸻

⚠️ Troubleshooting & Tips
	•	❗ If you see errors related to model loading, check Ollama is running and the model name in llama_generator.py matches your installed model.
	•	🔧 Update OLLAMA_API_URL in llama_generator.py if you changed the port or host.
	•	🆕 If you don’t have a git repo initialized, run git init first in your project folder.

⸻

🤝 How to Contribute?

Feel free to submit issues or pull requests to improve the model, add reinforcement learning features, or improve integration.

⸻

📄 License

MIT License © Venigalla Siva Srinivas