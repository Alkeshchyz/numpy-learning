import numpy as np

marks = np.array([45, 78, 92, 67, 88, 34, 95, 73, 81, 59])

print("Original marks:")
print(marks)

print("\nIndexes where marks are greater than 70:")
print(np.where(marks > 70))

print("\nMarks greater than 70:")
print(marks[np.where(marks > 70)])