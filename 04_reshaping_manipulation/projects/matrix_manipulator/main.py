import numpy as np

matrix = np.arange(1, 13)

print("Original array:")
print(matrix)
print("Original shape:", matrix.shape)

matrix_2d = matrix.reshape(3, 4)

print("\n3 × 4 Matrix:")
print(matrix_2d)
print("Shape:", matrix_2d.shape)

transposed = matrix_2d.T

print("\nTransposed Matrix:")
print(transposed)
print("Shape:", transposed.shape)

flattened = matrix_2d.flatten()

print("\nFlattened Matrix:")
print(flattened)
print("Shape:", flattened.shape)

raveled = np.ravel(matrix_2d)

print("\nRaveled Matrix:")
print(raveled)
print("Shape:", raveled.shape)


row_array = np.expand_dims(raveled, axis=0)
column_array = np.expand_dims(raveled, axis=1)

print("\nRow Array:")
print(row_array)
print("Shape:", row_array.shape)

print("\nColumn Array:")
print(column_array)
print("Shape:", column_array.shape)