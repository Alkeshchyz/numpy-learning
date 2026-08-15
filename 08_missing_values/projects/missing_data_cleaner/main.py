import numpy as np


def count_missing(data):
    return np.sum(np.isnan(data))


def replace_missing(data):
    mean_value = np.nanmean(data)
    return np.where(np.isnan(data), mean_value, data)


# Step 1 — Load dataset with NaN values
marks = np.array([78, 85, np.nan, 92, 67, np.nan, 88, 74, np.nan, 95])

print("Original data:")
print(marks)

# Step 2 — Count missing values
print("\nNumber of missing values:")
print(count_missing(marks))

# Step 3 — Impute missing values with mean
cleaned_marks = replace_missing(marks)

print("\nCleaned data:")
print(cleaned_marks)

# Step 4 — Verify missing values are removed
print("\nNumber of missing values after cleaning:")
print(count_missing(cleaned_marks))

# Step 5 — Compute summary statistics on cleaned data
print("\nMean of cleaned data:")
print(np.mean(cleaned_marks))

print("\nMedian of cleaned data:")
print(np.median(cleaned_marks))

print("\nStandard deviation of cleaned data:")
print(np.std(cleaned_marks))