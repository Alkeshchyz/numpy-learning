import numpy as np

# Step 5 Demonstration
marks = np.array([45, 67, 78, 82, 91])
print("Original marks:")
print(marks)

# In-place multi-index assignment
np.put(marks, [1, 3], [70, 95])
print("\nUpdated marks:")
print(marks)

# In-place single index assignment
np.put(marks, 2, 100)
print("\nUpdated marks (index 2 set to 100):")
print(marks)

print("\n" + "=" * 40 + "\n")

# ⭐ Mini-task
scores = np.array([50, 60, 70, 80, 90])
print("Original scores:")
print(scores)

# Update index 0 -> 55, index 2 -> 75, index 4 -> 95
np.put(scores, [0, 2, 4], [55, 75, 95])

print("\nUpdated scores:")
print(scores)