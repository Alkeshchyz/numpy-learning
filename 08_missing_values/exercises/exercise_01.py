import numpy as np

# 1. Original dataset
marks = np.array([78, 85, np.nan, 92, 67, np.nan, 88, 74, np.nan, 95])

print("Original marks:")
print(marks)
print()

# 2. Detect missing values
is_missing = np.isnan(marks)
print("Missing value positions (Boolean mask):")
print(is_missing)
print()

# 3. Count missing values
missing_count = np.sum(is_missing)
print("Number of missing values:")
print(missing_count)
print()

# 4. Calculate normal mean (results in nan due to missing values)
print("Normal Mean (with NaN):")
print(np.mean(marks))
print()

# 5. Calculate mean ignoring missing values
mean_marks = np.nanmean(marks)
print("Mean ignoring missing values:")
print(mean_marks)
print()

# 6. Calculate median and standard deviation ignoring missing values
print("Median ignoring missing values:")
print(np.nanmedian(marks))

print("Standard Deviation ignoring missing values:")
print(np.nanstd(marks))
print()

# 7. Replace missing values with the mean
cleaned_marks = np.where(np.isnan(marks), mean_marks, marks)
print("Cleaned marks:")
print(cleaned_marks)
print()

# ⭐ Challenge — Verify no missing values remain
remaining_missing = np.sum(np.isnan(cleaned_marks))
print("Remaining missing values count:")
print(remaining_missing)