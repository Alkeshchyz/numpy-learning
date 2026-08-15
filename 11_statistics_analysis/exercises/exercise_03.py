import numpy as np

# Number of hours students studied
study_hours = np.array([
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
])

# Corresponding exam marks
marks = np.array([
    42, 48, 55, 60, 67,
    72, 78, 84, 89, 94
])

# TODO:
# 1. Calculate the correlation between study hours and marks.
# 2. Calculate the mean study hours.
# 3. Calculate the mean marks.
# 4. Find the highest mark.
# 5. Find the lowest mark.
#
# Use:
# np.corrcoef()
# np.mean()
# np.max()
# np.min()

correlation = np.corrcoef(study_hours, marks)[0, 1]
mean_study_hours = np.mean(study_hours)
mean_marks = np.mean(marks)
highest_mark = np.max(marks)
lowest_mark = np.min(marks)

print("Correlation between study hours and marks:", correlation)
print("Mean study hours:", mean_study_hours)
print("Mean marks:", mean_marks)
print("Highest mark:", highest_mark)
print("Lowest mark:", lowest_mark)