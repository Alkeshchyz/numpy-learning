import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Original array:")
print(numbers)

updated = np.delete(numbers, 2)

print("\nAfter deleting index 2:")
print(updated)

updated = np.delete(numbers, [0, 4])

print("\nAfter deleting indices 0 and 4:")
print(updated)

print("\nOriginal array:")
print(numbers)

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nDelete row 1:")
print(np.delete(matrix, 1, axis=0))

print("\nDelete column 1:")
print(np.delete(matrix, 1, axis=1))