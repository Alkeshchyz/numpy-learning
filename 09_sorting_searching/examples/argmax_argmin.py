import numpy as np

# Mini-task dataset
marks = np.array([56, 91, 34, 78, 65, 88, 42, 99, 73, 61])

# 1. Sorted indices using np.argsort()
indices = np.argsort(marks)

# 2. Sorted marks
sorted_marks = marks[indices]

# 3 & 4. Highest mark and its index
highest_mark = np.max(marks)
highest_index = np.argmax(marks)

# 5 & 6. Lowest mark and its index
lowest_mark = np.min(marks)
lowest_index = np.argmin(marks)

# Print results
print("Original Marks:")
print(marks)

print("\nSorted indices:")
print(indices)

print("\nSorted marks:")
print(sorted_marks)

print("\nHighest mark:", highest_mark)
print("Position of highest mark:", highest_index)

print("\nLowest mark:", lowest_mark)
print("Position of lowest mark:", lowest_index)