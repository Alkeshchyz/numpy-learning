import numpy as np


# Task 1: Mean Squared Error function
def mean_squared_error(actual, predicted):
    return np.mean((actual - predicted) ** 2)


# Task 2: Sigmoid function
def sigmoid(array):
    return 1 / (1 + np.exp(-array))


# Dataset
actual = np.array([10, 20, 30, 40, 50])
predicted = np.array([12, 18, 29, 43, 48])

# Task 3: Calculate MSE
mse = mean_squared_error(actual, predicted)

# Task 4: Calculate prediction errors
errors = actual - predicted

# Task 5: Apply sigmoid to errors
sigmoid_errors = sigmoid(errors)

# Print outputs
print("Actual values:")
print(actual)

print("\nPredicted values:")
print(predicted)

print("\nMean Squared Error:")
print(mse)

print("\nPrediction Errors:")
print(errors)

print("\nSigmoid of Errors:")
print(sigmoid_errors)