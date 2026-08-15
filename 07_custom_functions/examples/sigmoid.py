import numpy as np


def sigmoid(array):
    return 1 / (1 + np.exp(-array))


values = np.array([-5, -2, -1, 0, 1, 2, 5])

result = sigmoid(values)

print("Input values:")
print(values)

print("\nSigmoid values:")
print(result)