import numpy as np

# Mini-task dataset
marks = np.array([56, 91, 34, 78, 65, 88, 42, 99, 73, 61])

# 1. Print original marks
print("Original marks:")
print(marks)

# 2. Sort in ascending order
ascending = np.sort(marks)
print("\nAscending marks:")
print(ascending)

# 3. Sort in descending order
descending = np.sort(marks)[::-1]
print("\nDescending marks:")
print(descending)

# 4. Verify that the original array is unchanged
print("\nOriginal marks after sorting operations:")
print(marks)