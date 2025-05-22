import torch
from rl.agent import DQNAgent
from rl.env import SimpleEnv

import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file for local testing

token = os.getenv("GH_PAT")

if not token:
    raise ValueError("GH_PAT not found in environment variables.")

# You can now use `token` in your GitHub-related logic
print("GitHub token loaded securely ✅")

def train_rl_agent():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    env = SimpleEnv()
    agent = DQNAgent(env.state_dim, env.action_dim, device)

    num_episodes = 500
    rewards = []

    for episode in range(num_episodes):
        state = env.reset()
        total_reward = 0

        for t in range(200):
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            agent.remember(state, action, reward, next_state, done)
            agent.replay()
            state = next_state
            total_reward += reward

            if done:
                break

        agent.update_target_model()
        rewards.append(total_reward)
        print(f"Episode {episode+1}/{num_episodes} - Reward: {total_reward:.2f}, Epsilon: {agent.epsilon:.2f}")

    # Plot rewards
    import matplotlib.pyplot as plt
    plt.plot(rewards)
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.title('Training Progress')
    plt.savefig('training_plot.png')
    plt.show()

if __name__ == "__main__":
    train_rl_agent()