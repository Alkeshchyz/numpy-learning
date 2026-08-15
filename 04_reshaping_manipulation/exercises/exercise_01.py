import numpy as np

# 1. Create and print the original 1D array
numbers = np.arange(1, 13)
print("Original Array:")
print(numbers)
print("Shape:", numbers.shape)
print()

# 2. Reshape into a 3x4 matrix
matrix_3x4 = numbers.reshape(3, 4)
print("3x4 Matrix:")
print(matrix_3x4)
print("Shape:", matrix_3x4.shape)
print()

# 3. Reshape into a 2x6 matrix
matrix_2x6 = numbers.reshape(2, 6)
print("2x6 Matrix:")
print(matrix_2x6)
print("Shape:", matrix_2x6.shape)
print()

# 4. Reshape into a 4x3 matrix
matrix_4x3 = numbers.reshape(4, 3)
print("4x3 Matrix:")
print(matrix_4x3)
print("Shape:", matrix_4x3.shape)