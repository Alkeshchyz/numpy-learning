import numpy as np


# ---------------------------------------------------------
# Student Dataset
# ---------------------------------------------------------

# Student marks collected from a class.
marks = np.array([
    45, 52, 60, 67, 72,
    78, 81, 85, 90, 95,
    55, 63, 70, 76, 88
])

# Number of hours each student studied.
study_hours = np.array([
    2, 2.5, 3, 3.5, 4,
    4.5, 5, 5.5, 6, 6.5,
    2.5, 3, 4, 4.5, 5.5
])


# ---------------------------------------------------------
# Basic Statistical Analysis
# ---------------------------------------------------------

print("========== BASIC STATISTICS ==========")

# Calculate the average mark.
mean_marks = np.mean(marks)

# Find the middle value of the dataset.
median_marks = np.median(marks)

# Calculate how much the marks vary around the mean.
standard_deviation = np.std(marks)

# Calculate the variance.
variance = np.var(marks)

# Find the minimum mark.
minimum_marks = np.min(marks)

# Find the maximum mark.
maximum_marks = np.max(marks)

print("Mean:", mean_marks)
print("Median:", median_marks)
print("Standard Deviation:", standard_deviation)
print("Variance:", variance)
print("Minimum:", minimum_marks)
print("Maximum:", maximum_marks)


# ---------------------------------------------------------
# Percentile Analysis
# ---------------------------------------------------------

print("\n========== PERCENTILE ANALYSIS ==========")

# Find important points in the distribution.
percentile_25 = np.percentile(marks, 25)
percentile_50 = np.percentile(marks, 50)
percentile_75 = np.percentile(marks, 75)
percentile_90 = np.percentile(marks, 90)

print("25th Percentile:", percentile_25)
print("50th Percentile:", percentile_50)
print("75th Percentile:", percentile_75)
print("90th Percentile:", percentile_90)


# ---------------------------------------------------------
# Cumulative Analysis
# ---------------------------------------------------------

print("\n========== CUMULATIVE ANALYSIS ==========")

# Calculate cumulative marks.
# Each value represents the running total.
cumulative_marks = np.cumsum(marks)

print("Cumulative marks:")
print(cumulative_marks)


# ---------------------------------------------------------
# Histogram Analysis
# ---------------------------------------------------------

print("\n========== HISTOGRAM ANALYSIS ==========")

# Define mark ranges.
bins = np.array([0, 50, 60, 70, 80, 90, 100])

# Count how many students fall into each range.
histogram, edges = np.histogram(marks, bins=bins)

print("Mark ranges:")
print(edges)

print("Students in each range:")
print(histogram)


# ---------------------------------------------------------
# Correlation Analysis
# ---------------------------------------------------------

print("\n========== CORRELATION ANALYSIS ==========")

# Calculate the correlation matrix between
# study hours and marks.
correlation_matrix = np.corrcoef(
    study_hours,
    marks
)

# Extract the actual correlation coefficient.
correlation = correlation_matrix[0, 1]

print("Correlation coefficient:")
print(correlation)


# ---------------------------------------------------------
# Final Interpretation
# ---------------------------------------------------------

print("\n========== SUMMARY ==========")

if correlation > 0.7:
    print("There is a strong positive relationship between")
    print("study hours and marks.")

elif correlation > 0.3:
    print("There is a moderate positive relationship between")
    print("study hours and marks.")

elif correlation < -0.3:
    print("There is a negative relationship between")
    print("study hours and marks.")

else:
    print("There is a weak or negligible relationship between")
    print("study hours and marks.")