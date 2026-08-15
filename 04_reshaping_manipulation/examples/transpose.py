import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Original matrix:")
print(matrix)

print("\nTranspose using np.transpose():")
print(np.transpose(matrix))

print("\nTranspose using .T:")
print(matrix.T)

print("\nOriginal shape:", matrix.shape)
print("Transposed shape:", matrix.T.shape)

matrix2 = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

print("\nOriginal matrix 2:")
print(matrix2)

print("\nTranspose of matrix 2:")
print(matrix2.T)
print("Shape of transposed matrix 2:", matrix2.T.shape)
