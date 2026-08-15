import numpy as np

# Student marks
marks = np.array([
    45, 52, 60, 67, 72,
    78, 81, 85, 90, 95,
    55, 63, 70, 76, 88
])

# Create bins representing mark ranges.
# Each bin groups values into a particular range.
bins = np.array([0, 50, 60, 70, 80, 90, 100])

# Count how many values fall into each bin.
histogram, edges = np.histogram(marks, bins=bins)

print("Marks:")
print(marks)

print("\nHistogram counts:")
print(histogram)

print("\nBin edges:")
print(edges)