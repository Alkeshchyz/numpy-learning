import numpy as np

# Step 5 Demonstration
marks = np.array([45, 67, 45, 82, 67, 91, 82, 45, 95])

print("Original marks:")
print(marks)

unique_marks = np.unique(marks)

print("\nUnique marks:")
print(unique_marks)

print("\nNumber of unique marks:")
print(len(unique_marks))

unique, counts = np.unique(marks, return_counts=True)

print("\nUnique values:")
print(unique)

print("\nNumber of occurrences:")
print(counts)

print("\n" + "=" * 40 + "\n")

# ⭐ Mini-task
scores = np.array([
    80, 90, 75, 80, 95,
    90, 85, 75, 100, 90
])

# Extract unique elements and their frequencies
unique_scores, score_counts = np.unique(scores, return_counts=True)

print("Original scores:")
print(scores)

print("\nUnique scores:")
print(unique_scores)

print("\nNumber of unique scores:")
print(len(unique_scores))

print("\nOccurrences per score:")
print("Scores: ", unique_scores)
print("Counts: ", score_counts)