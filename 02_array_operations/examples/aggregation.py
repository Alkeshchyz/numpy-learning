import numpy as np

a = np.array([10, 20, 30, 40, 50])

print("Sum:", np.sum(a))
print("Product:", np.prod(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))
print("Mean:", np.mean(a))
print("Standard Deviation:", np.std(a))
print("Variance:", np.var(a))

b = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Sum of b:", np.sum(b))
print("Product of b:", np.prod(b))
print("Minimum of b:", np.min(b))
print("Maximum of b:", np.max(b))
print("Mean of b:", np.mean(b))
print("Standard Deviation of b:", np.std(b))
print("Variance of b:", np.var(b))

print("Sum of b along axis 0:", np.sum(b, axis=0))
print("Sum of b along axis 1:", np.sum(b, axis=1))