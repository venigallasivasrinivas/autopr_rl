import random
import numpy as np

class SimpleEnv:
    def __init__(self):
        self.state_dim = 4
        self.action_dim = 2
        self.current_step = 0
        self.max_steps = 200

    def reset(self):
        self.current_step = 0
        # Return an initial state vector
        return np.zeros(self.state_dim, dtype=np.float32)

    def step(self, action):
        self.current_step += 1

        # Dummy next_state - random vector
        next_state = np.random.rand(self.state_dim).astype(np.float32)

        # Dummy reward - random float
        reward = random.random()

        # Done flag when max steps reached
        done = self.current_step >= self.max_steps

        # Additional info dictionary (empty)
        info = {}

        return next_state, reward, done, info