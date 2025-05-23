🚀 AutoPR RL Agent

AutoPR RL Agent is a reinforcement learning system that automatically trains an agent on every Pull Request (PR) update to your GitHub repo. This project brings continuous learning directly into your development workflow, using GitHub Actions and PyTorch-based RL agents.

⸻

🧠 What Is This Project?

AutoPR RL Agent connects GitHub PR events with a DQN-based Reinforcement Learning agent. Every time a developer opens or updates a PR, the RL agent is retrained using the latest state of the repository, encouraging adaptive learning through real-world development workflows.

⸻

✨ Key Features
	•	🎯 Reinforcement Learning agent using Deep Q-Network (DQN) in PyTorch
	•	🔁 Automated training triggered by GitHub Pull Requests
	•	🛠️ GitHub Actions integrated workflow (.github/workflows/train_agent.yml)
	•	📤 Auto-posts results to PRs as comments
	•	🔧 Easy setup, clean modular Python code
	•	💡 Extensible design for custom RL environments and agents

⸻

🚀 Getting Started

Prerequisites
	•	Python 3.9+
	•	GitHub repository with Actions enabled
	•	GitHub Personal Access Token (GH_PAT) with appropriate scopes

⸻

🔧 Installation

Follow these steps to set up the project locally:

1. Clone the Repository

git clone https://github.com/venigallasivasrinivas/autopr_rl.git
cd autopr_rl

2. Create and Activate a Virtual Environment

macOS/Linux:

python -m venv venv
source venv/bin/activate

Windows:

python -m venv venv
venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Set Your GitHub Token

You’ll need to set a GitHub Personal Access Token to enable GitHub API interactions.
👉 See the next section: 🔐 Setting Up GitHub Personal Access Token (GH_PAT)

⸻

🔐 Setting Up GitHub Personal Access Token (GH_PAT)

To allow GitHub API interactions (like commenting on PRs), you must create and configure a token:

1. Generate a Token
	•	Go to: https://github.com/settings/tokens
	•	Click “Generate new token (classic)”
	•	Enable:
	•	repo
	•	(Optional) workflow for advanced control
	•	Copy and store your token securely

2. Set GH_PAT Locally

Linux/macOS:

export GH_PAT="your_token_here"

To persist:

echo 'export GH_PAT="your_token_here"' >> ~/.bashrc
source ~/.bashrc

Windows CMD:

set GH_PAT=your_token_here

Windows PowerShell:

$env:GH_PAT="your_token_here"

3. Add to GitHub Actions
	•	Go to Repo > Settings > Secrets and Variables > Actions
	•	Click New repository secret
	•	Name: GH_PAT
	•	Value: your token

Then reference it inside .github/workflows/train_agent.yml:

env:
  GH_PAT: ${{ secrets.GH_PAT }}


⸻

🧪 How It Works
	•	A PR is opened or updated.
	•	GitHub Actions triggers the RL training job.
	•	The RL agent (DQNAgent) trains using your repo as the environment.
	•	Training success and basic results are posted as comments on the PR.

⸻

🧠 RL Agent Summary
	•	Agent: DQNAgent with replay buffer, epsilon-greedy exploration
	•	Library: PyTorch
	•	Environment: Custom GitHub PR environment (env.py)
	•	Training Loop: Modular and customizable (rl_autopr.py)

⸻

🛠 Usage

Train Locally

python -m rl.rl_autopr

Make sure GH_PAT is set for GitHub access.

⸻

🤝 Contributing

I welcome contributions!
	•	Open issues
	•	Create pull requests
	•	Suggest improvements to RL logic or GitHub integrations

⸻

📜 License

This project is licensed under the MIT License.

⸻

👨‍💻 Author

Venigalla Siva Srinivas
Reinforcement Learning Enthusiast | Developer | Innovator
