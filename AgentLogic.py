import numpy as np
import tensorflow as tf

from NN import NeuralNetwork, Memory
from config import GAMMA
from config import BUFFER_SIZE, BATCH_SIZE
from config import EPSILON, EPSILON_MIN, EPSILON_INTERVAL
from config import EPSILON_GREEDY_FRAMES, EPSILON_RANDOM_FRAMES


class AgentLogic:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size

        self.brain = NeuralNetwork(self.state_size, self.action_size)
        self.brain_target = NeuralNetwork(self.state_size, self.action_size)

        self.memory = Memory(BUFFER_SIZE)

        self.epsilon = EPSILON

    def sync_target_weights(self):
        self.brain_target.model.set_weights(self.brain.model.get_weights())

    def decrease_epsilon(self):
        self.epsilon -= EPSILON_INTERVAL / EPSILON_GREEDY_FRAMES
        self.epsilon = max(self.epsilon, EPSILON_MIN)

    def get_guess(self, input_data):
        # Predict action Q-values
        # From environment state
        state_tensor = tf.convert_to_tensor(input_data)
        state_tensor = tf.expand_dims(state_tensor, 0)
        action_prob = self.brain.model(state_tensor, training=False)
        # Take best action
        action = tf.argmax(action_prob[0]).numpy()

        return action

    def choose_action(self, input_data, frame_count):
        if frame_count < EPSILON_RANDOM_FRAMES or self.epsilon > np.random.rand(1)[0]:
            # Take random action
            action = np.random.choice(self.action_size)
        else:
            # Predict action Q-values
            action = self.get_guess(input_data)

        return action

    def add_to_memory(self, action, state, next_state, reward, done):
        self.memory.add(action, state, next_state, reward, done)

    def train(self):
        actions, states, next_states, rewards, dones = self.memory.sample(BATCH_SIZE)

        dones = tf.convert_to_tensor(dones)

        # Build the updated Q-values for the sampled future states
        # Use the target model for stability
        future_rewards = self.brain_target.model.predict(next_states)
        # Q value = reward + discount factor * expected future reward
        updated_q_values = rewards + GAMMA * tf.reduce_max(
            future_rewards, axis=1
        )

        # If final frame set the last value to -1
        updated_q_values = updated_q_values * (1 - dones) - dones

        # Create a mask so we only calculate loss on the updated Q-values
        masks = tf.one_hot(actions, self.action_size)

        with tf.GradientTape() as tape:
            # Train the model on the states and updated Q-values
            q_values = self.brain.model(states)

            # Apply the masks to the Q-values to get the Q-value for action taken
            q_action = tf.reduce_sum(tf.multiply(q_values, masks), axis=1)
            # Calculate loss between new Q-value and old Q-value
            loss = self.brain.loss_function(updated_q_values, q_action)

        # Backpropagation
        grads = tape.gradient(loss, self.brain.model.trainable_variables)
        self.brain.optimizer.apply_gradients(zip(grads, self.brain.model.trainable_variables))
