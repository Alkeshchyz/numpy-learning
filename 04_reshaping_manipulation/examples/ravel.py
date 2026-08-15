import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Original matrix:")
print(matrix)

raveled = np.ravel(matrix)

print("\nRaveled array:")
print(raveled)

print("\nOriginal shape:", matrix.shape)
print("Raveled shape:", raveled.shape)