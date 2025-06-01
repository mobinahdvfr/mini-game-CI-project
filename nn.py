import numpy as np

class NeuralNetwork():

    def __init__(self, layer_sizes):

        # TODO

        # random weights for layer 1 and 2
        self.w1 = np.random.randn(layer_sizes[1], layer_sizes[0])
        self.w2 = np.random.randn(layer_sizes[2], layer_sizes[1])
        # bias vectors for layer 1 and 2 (zero vector)
        self.b1 = np.zeros((layer_sizes[1], 1))
        self.b2 = np.zeros((layer_sizes[2], 1))

        # layer_sizes example: [4, 10, 2]
        pass

    def activation(self, x):

        # TODO

        # sigmoid
        return np.divide(1, np.add(1, np.exp(-x)))

        return x

    def forward(self, x):

        # TODO

        # sigma(wx) + b and activation for hidden and last layer
        hidden_layer = self.activation(np.add(np.dot(self.w1, x), self.b1))
        output = self.activation(np.add(np.dot(self.w2, hidden_layer), self.b2))
        if output < 0.5:
            return -1
        else:
            return 1

        # x example: np.array([[0.1], [0.2], [0.3]])
        pass
