import numpy as np

# Original dataset
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 88]
])

bonus = np.array([5, 10, 15])
weights = np.array([1.1, 1.2, 1.3])

# Print shapes
print("Marks shape:", marks.shape)
print("Bonus shape:", bonus.shape)
print("Weights shape:", weights.shape)
print()

# 1. Add the bonus to every student's marks
print("Marks + Bonus:")
print(marks + bonus)
print()

# 2. Subtract the bonus from every student's marks
print("Marks - Bonus:")
print(marks - bonus)
print()

# 3. Multiply every subject's marks by weights
print("Marks * Weights:")
print(marks * weights)