import numpy as np

# Student IDs collected from multiple sources.
student_ids = np.array([
    101, 102, 103, 103, 104,
    105, 106, 106, 107, 108,
    108, 109, 110, 110
])

# 1. Find all unique student IDs
unique_ids = np.unique(student_ids)

# 2. Find the total number of unique students
total_unique = unique_ids.size

# 3. Find how many IDs were duplicated
duplicated_count = student_ids.size - unique_ids.size

# Display results
print("1. Unique student IDs:")
print(unique_ids)

print("\n2. Total number of unique students:")
print(total_unique)

print("\n3. Number of duplicated IDs:")
print(duplicated_count)