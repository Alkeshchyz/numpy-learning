import numpy as np

# Example 1: Restricting marks to [0, 100]
marks = np.array([25, 45, 67, 82, 105, 120, 55, 30])
print("Original marks:")
print(marks)

clipped_marks = np.clip(marks, 0, 100)
print("\nClipped marks:")
print(clipped_marks)

# Example 2: Restricting temperatures to [0, 40]
temperatures = np.array([-10, 5, 15, 25, 35, 45])
limited = np.clip(temperatures, 0, 40)

print("\nOriginal temperatures:")
print(temperatures)
print("\nLimited temperatures:")
print(limited)

print("\n" + "=" * 40 + "\n")

# ⭐ Mini-task
scores = np.array([-20, 35, 55, 75, 110, 150])
print("Original scores:")
print(scores)

# Clipped between 0 and 100
scores_0_100 = np.clip(scores, 0, 100)
print("\nScores clipped (0 to 100):")
print(scores_0_100)

# Clipped between 40 and 80
scores_40_80 = np.clip(scores, 40, 80)
print("\nScores clipped (40 to 80):")
print(scores_40_80)