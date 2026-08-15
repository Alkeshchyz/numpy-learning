import numpy as np

# Step 1 — Dataset
marks = np.array([45, 78, 92, 67, 88, 34, 95, 73, 81, 59])
print("Student Marks:")
print(marks)

# Step 2 — Filter passing students
passing = marks[marks >= 60]
print("\nPassing Marks:")
print(passing)

# Step 3 — Find failing marks
failing = marks[marks < 60]
print("\nFailing Marks:")
print(failing)

# Step 4 — Find high performers
high_performers = marks[marks >= 80]
print("\nHigh Performers:")
print(high_performers)

# Step 5 — Use np.where()
result = np.where(marks >= 60, "Pass", "Fail")
print("\nPass/Fail Status:")
print(result)

# Step 6 — Find highest and lowest
highest = np.max(marks)
lowest = np.min(marks)
highest_index = np.argmax(marks)
lowest_index = np.argmin(marks)

print("\nHighest Mark:", highest)
print("Highest Mark Index:", highest_index)
print("Lowest Mark:", lowest)
print("Lowest Mark Index:", lowest_index)

# Step 7 — Find marks between 70 and 90
middle_range = marks[(marks >= 70) & (marks <= 90)]
print("\nMarks Between 70 and 90:")
print(middle_range)