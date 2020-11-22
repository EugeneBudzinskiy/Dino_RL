import numpy as np
import tensorflow as tf
from tensorflow import keras

from config import LEARNING_RATE


class NeuralNetwork:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size

        self.hidden_size_1 = 512
        self.hidden_size_2 = 256

        inputs = keras.layers.Input(shape=(input_size,))
        layer1 = keras.layers.Dense(self.hidden_size_1, activation="relu")(inputs)
        layer2 = keras.layers.Dense(self.hidden_size_2, activation="relu")(layer1)
        outputs = keras.layers.Dense(self.output_size, activation="linear")(layer2)

        self.model = keras.Model(inputs=inputs, outputs=outputs)

        self.optimizer = keras.optimizers.Adam(learning_rate=LEARNING_RATE, clipnorm=1.0)
        self.loss_function = keras.losses.Huber()


class Memory:
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size

        self.__action_array = None
        self.__state_array = None
        self.__next_state_array = None
        self.__reward_array = None
        self.__done_array = None

    def __len__(self):
        return len(self.__done_array)

    def add(self, action, state, next_state, reward, done):
        """Add a new experience to memory."""

        if self.__done_array is None:
            self.__action_array = np.array([action])
            self.__state_array = np.array([state])

            self.__next_state_array = np.array([next_state])
            self.__reward_array = np.array([reward])
            self.__done_array = np.array([done])

        else:
            if self.__len__() >= self.buffer_size:
                self.__action_array = np.delete(self.__action_array, 0, axis=0)
                self.__state_array = np.delete(self.__state_array, 0, axis=0)
                self.__next_state_array = np.delete(self.__next_state_array, 0, axis=0)
                self.__reward_array = np.delete(self.__reward_array, 0, axis=0)
                self.__done_array = np.delete(self.__done_array, 0, axis=0)

            self.__action_array = np.append(self.__action_array, action)
            self.__state_array = np.append(self.__state_array, [state], axis=0)
            self.__next_state_array = np.append(self.__next_state_array, [next_state], axis=0)
            self.__reward_array = np.append(self.__reward_array, reward)
            self.__done_array = np.append(self.__done_array, done)

    def sample(self, batch_size):
        """Randomly sample a batch of experiences from memory."""
        indices = np.random.choice(self.__len__(), batch_size)

        actions = [self.__action_array[i] for i in indices]
        states = np.array([self.__state_array[i] for i in indices])
        next_states = np.array([self.__next_state_array[i] for i in indices])
        rewards = [self.__reward_array[i] for i in indices]
        dones = tf.convert_to_tensor(
            [float(self.__done_array[i]) for i in indices]
        )

        return actions, states, next_states, rewards, dones
