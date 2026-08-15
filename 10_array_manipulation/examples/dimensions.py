import numpy as np

# 1D array
array_1d = np.array([10, 20, 30, 40])

print("1D array:")
print(array_1d)

print("\nNumber of dimensions:")
print(np.ndim(array_1d))

print("\nShape:")
print(array_1d.shape)

print("\nSize:")
print(array_1d.size)


# 2D array
array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D array:")
print(array_2d)

print("\nNumber of dimensions:")
print(np.ndim(array_2d))

print("\nShape:")
print(array_2d.shape)

print("\nSize:")
print(array_2d.size)