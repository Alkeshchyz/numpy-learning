import numpy as np


def mean_squared_error(actual, predicted):
    error = actual - predicted
    squared_error = error ** 2

    return np.mean(squared_error)


actual = np.array([10, 20, 30, 40, 50])
predicted = np.array([12, 18, 29, 43, 48])

mse = mean_squared_error(actual, predicted)

print("Actual values:")
print(actual)

print("\nPredicted values:")
print(predicted)

print("\nMean Squared Error:")
print(mse)