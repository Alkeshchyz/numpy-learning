import numpy as np

data = np.array([10, 20, np.nan, 40, 50, np.nan, 70])

print("Original data:")
print(data)

print("\nMissing values:")
print(np.isnan(data))

print("\nNumber of missing values:")
print(np.sum(np.isnan(data)))

print("\nMean with NaN:")
print(np.mean(data))

print("\nMean ignoring NaN:")
print(np.nanmean(data))