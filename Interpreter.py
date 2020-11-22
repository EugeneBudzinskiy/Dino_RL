from collections import deque

from config import EPISODE_COUNT


class Interpreter:
    def __init__(self):
        self.state_size = 4
        self.action_size = 3

        self.reward_window = deque(maxlen=100)
        self.running_reward = 0
        self.frame_count = 0

    def train_cycle(self):
        for i_episode in range(1, EPISODE_COUNT + 1):
            pass


