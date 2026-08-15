import numpy as np

numbers = np.arange(1, 13)

print("Original array:")
print(numbers)

matrix = numbers.reshape(3, 4)

print("Reshaped array:")
print(matrix)

print("Shape:", matrix.shape)

matrix = numbers.reshape(2, 6)
print("Reshaped array (2, 6):")
print(matrix)

numbers.reshape(4, 3)
print("Reshaped array (4, 3):")
print(numbers.reshape(4, 3))

matrix = numbers.reshape(1, 12)
print("Reshaped array (1, 12):")
print(matrix)