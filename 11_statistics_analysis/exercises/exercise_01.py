import numpy as np

# Student marks
marks = np.array([
    42, 55, 61, 67, 70,
    74, 78, 82, 88, 91,
    95, 99
])

# TODO:
# 1. Calculate the 25th percentile.
# 2. Calculate the 50th percentile.
# 3. Calculate the 75th percentile.
# 4. Calculate the 90th percentile.
# 5. Print all results clearly.

# Use:
# np.percentile()
percentile_25 = np.percentile(marks, 25)
percentile_50 = np.percentile(marks, 50)
percentile_75 = np.percentile(marks, 75)
percentile_90 = np.percentile(marks, 90)

print("25th Percentile:", percentile_25)
print("50th Percentile:", percentile_50)
print("75th Percentile:", percentile_75)
print("90th Percentile:", percentile_90)