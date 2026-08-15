import numpy as np

# Number of hours students studied
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Corresponding exam marks
marks = np.array([45, 50, 55, 62, 68, 75, 82, 90])

# Calculate the correlation coefficient.
# np.corrcoef() returns a correlation matrix.
correlation_matrix = np.corrcoef(study_hours, marks)

print("Correlation matrix:")
print(correlation_matrix)

# Extract the correlation coefficient between
# study hours and marks.
correlation = correlation_matrix[0, 1]

print("\nCorrelation coefficient:")
print(correlation)