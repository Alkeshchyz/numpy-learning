import numpy as np

numbers = np.array([10, 20, 30, 40])

print("Original array:")
print(numbers)

print("Original shape:", numbers.shape)

row_array = np.expand_dims(numbers, axis=0)

print("\nAfter expand_dims(axis=0):")
print(row_array)
print("Shape:", row_array.shape)

column_array = np.expand_dims(numbers, axis=1)

print("\nAfter expand_dims(axis=1):")
print(column_array)
print("Shape:", column_array.shape)