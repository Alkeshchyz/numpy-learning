import numpy as np

# Input arrays
scores = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 88]
])

bonus = np.array([
    [5],
    [10],
    [15]
])

multiplier = np.array([
    [1.1],
    [1.2],
    [1.3]
])

# Print shapes
print("Scores shape:", scores.shape)
print("Bonus shape:", bonus.shape)
print("Multiplier shape:", multiplier.shape)
print()

# 1. Add bonus to scores (Row-wise adjustment)
print("Scores + Bonus:")
print(scores + bonus)
print()

# 2. Subtract bonus from scores
print("Scores - Bonus:")
print(scores - bonus)
print()

# 3. Multiply scores by multiplier
print("Scores * Multiplier:")
print(scores * multiplier)

# Broadcasting Explanation:
# - scores shape: (3, 3)
# - bonus shape: (3, 1)
# - multiplier shape: (3, 1)
# Broadcasting works here because when comparing dimensions from right to left, 
# the second dimension is 1. NumPy automatically stretches the (3, 1) column 
# array across all 3 columns to match the (3, 3) matrix.