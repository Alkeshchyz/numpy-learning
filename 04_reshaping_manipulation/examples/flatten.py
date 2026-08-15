import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Original matrix:")
print(matrix)

flat = matrix.flatten()

print("\nFlattened array:")
print(flat)

print("\nOriginal shape:", matrix.shape)
print("Flattened shape:", flat.shape)

matrix2 = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

print("\nOriginal matrix 2:")
print(matrix2)

flat2 = matrix2.flatten()
print("\nFlattened array 2:")
print(flat2)
print("Shape of flattened array 2:", flat2.shape)
