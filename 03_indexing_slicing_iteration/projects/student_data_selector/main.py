import numpy as np

students = np.array([
    [101, 78, 85, 92],
    [102, 65, 70, 75],
    [103, 88, 91, 95],
    [104, 55, 60, 68],
    [105, 90, 87, 93]
])

print("Student Data:")
print(students)

print("\nStudent IDs:", students[:, 0])  # All rows, first column
print("Subject 1 marks:", students[:, 1])  # All rows, second column
print("Subject 2 marks:", students[:, 2])  # All rows, third column
print("Subject 3 marks:", students[:, 3])  # All rows, fourth column

print("the first three students:\n", students[:3])  # First three rows
print("the last two students:\n", students[-2:])  # Last two rows
print("only the marks, excluding student IDs:\n", students[:, 1:4])  # All rows, columns from index 1 to 3

print("to print every value individually using np.nditer():")
for value in np.nditer(students):
    print(value)
