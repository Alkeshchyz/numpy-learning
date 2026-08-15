import numpy as np

# Student marks
marks = np.array([45, 52, 60, 67, 72, 78, 81, 85, 90, 95])

# Calculate the 25th percentile.
# 25% of the data falls below this value.
print("25th Percentile:", np.percentile(marks, 25))

# Calculate the 50th percentile.
# The 50th percentile is equivalent to the median.
print("50th Percentile:", np.percentile(marks, 50))

# Calculate the 75th percentile.
print("75th Percentile:", np.percentile(marks, 75))

# Calculate the 90th percentile.
print("90th Percentile:", np.percentile(marks, 90))