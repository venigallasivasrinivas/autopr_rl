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
	1.	Clone the repository

git clone https://github.com/venigallasivasrinivas/autopr_rl.git
cd autopr_rl

	2.	Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

	3.	Install dependencies

pip install -r requirements.txt

	4.	Set your GitHub token
See next section below 👇

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

📂 Project Structure

autopr_rl/
├── rl/
│   ├── agent.py            # DQN agent implementation
│   ├── env.py              # RL environment interacting with PRs
│   ├── rl_autopr.py        # Training loop for AutoPR agent
│   ├── llama_generator.py  # Optional language model integration
│   └── git_utils.py        # GitHub helper functions
├── .github/
│   └── workflows/
│       └── train_agent.yml # CI/CD workflow for training agent on PRs
├── main.py                 # (Optional) entry point
├── requirements.txt
├── .gitignore
└── README.md


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

We welcome contributions!
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
