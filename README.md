🚀 AutoPR RL Agent

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/venigallasivasrinivas/autopr_rl/train_agent.yml?branch=main)

AutoPR RL Agent is a reinforcement learning system that automatically trains an agent on every Pull Request (PR) update to your GitHub repo. This project brings continuous learning directly into your development workflow, using GitHub Actions and PyTorch-based RL agents.

⸻

🧠 What Is This Project?

AutoPR RL Agent connects GitHub PR events with a DQN-based Reinforcement Learning agent. Every time a developer opens or updates a PR, the RL agent is retrained using the latest state of the repository, encouraging adaptive learning through real-world development workflows.

⸻

🧠 Reinforcement Learning in AutoPR RL Agent

This project uses Reinforcement Learning (RL) to enable an AI agent to learn and improve automatically by interacting with its environment—in this case, the changes and feedback from GitHub Pull Requests (PRs).

What is Reinforcement Learning?

Reinforcement Learning is a type of machine learning where an agent learns to make decisions by performing actions and receiving feedback in the form of rewards or penalties. Over time, the agent aims to maximize its cumulative reward by learning optimal policies through trial and error.

How Reinforcement Learning is Applied Here
	•	Agent: The AI component that learns from PR data.
	•	Environment: The GitHub repository and its pull requests.
	•	Actions: Training updates triggered on new PRs, model adjustments, or improvements.
	•	Rewards: Implicit feedback from successful training runs and improved agent performance.

Using Deep Q-Learning (DQN), the agent approximates the best actions to take (like which model parameters to update or which training steps to prioritize) based on the state of the repository and code changes.

Why RL for AutoPR?
	•	Continuous Learning: The agent iteratively trains whenever a new PR is opened or updated, adapting to new code changes and learning from them.
	•	Automation: Reduces manual intervention by automating training and fine-tuning processes.
	•	Improved Model Performance: By learning from developer workflows and feedback loops, the AI model continually evolves, potentially increasing accuracy and efficiency in handling PRs.

This setup serves as a foundation for building more complex reward mechanisms and richer training loops, turning PRs into a dynamic training ground for smarter AI agents.

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

MIT License

Copyright (c) 2025 Venigalla Siva Srinivas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

⸻

👨‍💻 Author

Venigalla Siva Srinivas
Reinforcement Learning Enthusiast | Developer | Innovator
