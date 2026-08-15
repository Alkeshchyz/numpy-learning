import numpy as np

a = np.arange(1, 13)  # Create a NumPy array with values from 1 to 12
print(a)  # [ 1  2  3  4  5  6  7  8  9 10 11 12]

a = a.reshape(3, 4)  # Reshape the array to a 3x4 matrix
print(a)  # [[ 1  2  3  4]
        #  [ 5  6  7  8]
        #  [ 9 10 11 12]]

print(a.ndim)  # 2
print(a.shape)  # (3, 4)
print(a.size)  # 12

a = a.reshape(2,6)  # Reshape the array to a 2x6 matrix
print(a)  # [[ 1  2  3  4  5  6]
        #  [ 7  8  9 10 11 12]]
print(a.ndim)  # 2
print(a.shape)  # (2, 6)
print(a.size)  # 12