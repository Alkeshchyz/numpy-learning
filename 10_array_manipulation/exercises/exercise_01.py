import numpy as np

# ==========================================
# Exercise 01 — Append & Concatenate
# ==========================================
print("=== Exercise 01 — Append & Concatenate ===")

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

# 1. Append 70 to array a
step1 = np.append(a, 70)
print("Append 70 to 'a':", step1)

# 2. Append [80, 90] to the result
step2 = np.append(step1, [80, 90])
print("Append [80, 90] to result:", step2)

# 3. Concatenate a and b
concatenated = np.concatenate((a, b))
print("Concatenate 'a' and 'b':", concatenated)

print("\n" + "=" * 45 + "\n")

# ==========================================
# Exercise 02 — Delete & Dimensions
# ==========================================
print("=== Exercise 02 — Delete & Dimensions ===")

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original Data:\n", data)
print("\nDimensions:", np.ndim(data))
print("Shape:", data.shape)
print("Size:", data.size)

# Delete row 1 (axis=0)
deleted_row1 = np.delete(data, 1, axis=0)
print("\nAfter deleting Row 1:\n", deleted_row1)

# Delete column 0 (axis=1)
deleted_col0 = np.delete(data, 0, axis=1)
print("\nAfter deleting Column 0:\n", deleted_col0)

print("\n" + "=" * 45 + "\n")

# ==========================================
# Exercise 03 — Unique Values & Frequency
# ==========================================
print("=== Exercise 03 — Unique Values & Frequency ===")

scores = np.array([
    75, 80, 90, 75, 85,
    90, 80, 95, 75, 85,
    100, 90
])

# Extract unique elements and counts
unique_scores, counts = np.unique(scores, return_counts=True)

print("Unique scores:", unique_scores)
print("Number of unique scores:", len(unique_scores))
print("\nFrequency breakdown:")
for score, count in zip(unique_scores, counts):
    print(f"  Score {score}: {count} time(s)")

# ⭐ Challenge: Most frequent score via np.argmax()
most_frequent_idx = np.argmax(counts)
most_frequent_score = unique_scores[most_frequent_idx]
print(f"\nMost frequent score: {most_frequent_score} (Count: {counts[most_frequent_idx]})")