import numpy as np

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

print("Array A:")
print(a)

print("\nArray B:")
print(b)

combined = np.concatenate((a, b))

print("\nConcatenated array:")
print(combined)



matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

print("\nConcatenate by rows:")
print(np.concatenate((matrix1, matrix2), axis=0))

print("\nConcatenate by columns:")
print(np.concatenate((matrix1, matrix2), axis=1))