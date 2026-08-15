import numpy as np

scores = np.array([
    [70, 85, 90],
    [95, 60, 88],
    [75, 92, 80]
])

# 1 & 2. Overall max and min values
print("Highest score overall:", np.max(scores))
print("Lowest score overall:", np.min(scores))

# 3 & 4. Overall max and min index (flattened array index)
print("Index of highest score overall:", np.argmax(scores))
print("Index of lowest score overall:", np.argmin(scores))

# 5 & 6. Column-wise max values and their indexes (axis=0)
print("Highest score per column:", np.max(scores, axis=0))
print("Index of highest score per column:", np.argmax(scores, axis=0))

# 7 & 8. Row-wise max values and their indexes (axis=1)
print("Highest score per row:", np.max(scores, axis=1))
print("Index of highest score per row:", np.argmax(scores, axis=1))