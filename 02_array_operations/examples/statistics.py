import numpy as np

marks = np.array([45, 78, 92, 67, 88, 34, 95, 73, 81, 59])

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))
print("Variance:", np.var(marks))

print("difference between highest and lowest marks:", np.ptp(marks))  # Peak to peak (max - min)