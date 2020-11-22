import numpy as np
from collections import deque

from Game import GameEngine
from Interpreter import Interpreter
from config import BATCH_SIZE
from config import EPISODE_COUNT, MAX_STEPS_PER_EPISODE
from config import UPDATE_AFTER_FRAME, SYNC_AFTER_FRAME

engine = GameEngine()


def main():
    engine.menu.set_process_func(process)
    engine.menu.start_menu()


def process():
    if engine.is_human:
        while engine.is_running:
            engine.render()

            action = engine.get_action_from_key_check()
            engine.step(action)

    else:

        state_size = 4
        action_size = 3

        agent = Interpreter(state_size, action_size)
        reward_window = deque(maxlen=100)
        running_reward = 0
        frame_count = 0

        for i_episode in range(1, EPISODE_COUNT + 1):
            engine.setup()
            state = engine.get_state()

            episode_reward = 0

            for t in range(1, MAX_STEPS_PER_EPISODE + 1):
                # engine.render()  # Adding this line would show the attempts
                frame_count += 1

                # Use epsilon-greedy for exploration
                action = agent.choose_action(state, frame_count)

                # Decay probability of taking random action
                agent.decrease_epsilon()

                # Apply the sampled action in our environment
                engine.step(action)
                next_state, reward, done = engine.get_all_info()
                episode_reward += reward

                # Save actions and states in replay buffer
                agent.add_to_memory(action, state, next_state, reward, done)
                state = next_state

                # Update every fourth frame
                if frame_count % UPDATE_AFTER_FRAME == 0 and len(agent.memory) > BATCH_SIZE:
                    agent.train()

                if frame_count % SYNC_AFTER_FRAME == 0:
                    # update the the target network with new weights
                    agent.sync_target_weights()

                    # Log details
                    template = "running reward: {:.2f} at episode {}, frame count {}"
                    print(template.format(running_reward, i_episode, frame_count))

                if not engine.is_alive:
                    break

            reward_window.append(episode_reward)
            running_reward = np.mean(reward_window)

            if running_reward > 100000:
                print("FINISHING...")
                break


if __name__ == '__main__':
    main()
