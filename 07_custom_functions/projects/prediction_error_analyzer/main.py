import numpy as np


# Step 2 — Create the MSE function
def mean_squared_error(actual, predicted):
    error = actual - predicted
    squared_error = error**2
    return np.mean(squared_error)


# Step 3 — Create the Sigmoid function
def sigmoid(array):
    return 1 / (1 + np.exp(-array))


# Step 1 — Import NumPy and create the data
actual = np.array([10, 20, 30, 40, 50])
predicted = np.array([12, 18, 29, 43, 48])

print("Actual values:")
print(actual)

print("\nPredicted values:")
print(predicted)

# Step 4 — Calculate prediction errors
errors = actual - predicted
print("\nPrediction Errors:")
print(errors)

# Step 5 — Calculate MSE
mse = mean_squared_error(actual, predicted)
print("\nMean Squared Error:")
print(mse)

# Step 6 — Apply sigmoid to the errors
sigmoid_errors = sigmoid(errors)
print("\nSigmoid of Prediction Errors:")
print(sigmoid_errors)

# Step 7 — Absolute errors and MAE
absolute_errors = np.abs(errors)
print("\nAbsolute Errors:")
print(absolute_errors)

mean_absolute_error = np.mean(absolute_errors)
print("\nMean Absolute Error:")
print(mean_absolute_error)