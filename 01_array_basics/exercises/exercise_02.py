import numpy as np

a = np.array([10, 20, 30, 40, 50])  # Create a NumPy 1D array
print(a)  # [10 20 30 40 50]
print(a.dtype)  # int64

a = a.astype(np.float64)  # Convert the array to float64 data type
print(a)  # [10. 20. 30. 40. 50.]
print(a.dtype)  # float64

a = a.astype(np.int32)  # Convert the array to int32 data type
print(a)  # [10 20 30 40 50]
print(a.dtype)  # int32 (Note: The original array 'a' remains float64 because astype() returns a new array and does not modify the original array in place)
