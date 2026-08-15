import numpy as np

# Define the original 2D matrix
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# 1. Print the original matrix and its shape
print("Original Matrix:")
print(matrix)
print("Original Shape:", matrix.shape)
print()

# 2. Transpose the matrix using .T and print its shape
transposed = matrix.T
print("Transposed Matrix:")
print(transposed)
print("Transposed Shape:", transposed.shape)
print()

# 3. Flatten the matrix using .flatten() and print its shape
flattened = matrix.flatten()
print("Flattened Array:")
print(flattened)
print("Flattened Shape:", flattened.shape)