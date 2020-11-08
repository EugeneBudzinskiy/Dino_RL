import numpy as np

from CustomException import SaveNNException


class Brain:
    def __init__(self):
        self.is_trained = False
        self.count = 0

        self.weights_1 = np.array([1])
        self.weights_2 = np.array([2])

    def get_weights(self):
        if not self.is_trained:
            raise SaveNNException
        else:
            return np.array([
                self.weights_1,
                self.weights_2
            ], dtype=object)


class Memory:
    def __init__(self):
        self.memory = np.array([])
