import numpy as np

marks = np.array([45, 78, 92, 67, 88, 34, 95, 73, 81, 59])

print("Original marks:")
print(marks)

print("\nMarks greater than 70:")
print(marks[marks > 70])

print("\nMarks less than 50:")
print(marks[marks < 50])

print("\nEven marks:")
print(marks[marks % 2 == 0])