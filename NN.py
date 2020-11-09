import numpy as np

from CustomException import SaveNNException


class Brain:
    def __init__(self):
        self.input_node_count = 8
        self.hidden_node_count = 24
        self.output_node_count = 3

        # self.is_trained = False
        self.is_trained = True

        self.weights_1 = np.random.random((self.hidden_node_count, self.input_node_count))
        self.weights_2 = np.random.random((self.output_node_count, self.hidden_node_count))

    def get_weights(self):
        if not self.is_trained:
            raise SaveNNException
        else:
            name = [
                'weights_1',
                'weights_2'
            ]
            data = [
                self.weights_1.tolist(),
                self.weights_2.tolist()
            ]
            return dict(zip(name, data))

    def set_weights(self, json_weights):
        self.weights_1 = np.array(json_weights['weights_1'])
        self.weights_2 = np.array(json_weights['weights_2'])


class Memory:
    def __init__(self):
        self.memory = np.array([])
