import numpy as np

# --- Dimensions (np.ndim) ---Number of dimensions
print(np.ndim(np.array([1, 2, 3, 4, 5])))  # Output: 1
print(np.ndim(np.array([[1, 2, 3], [4, 5, 6]])))  # Output: 2
print(np.ndim(np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])))  # Output: 3

# --- Shape (np.shape) ---
print(np.shape(np.array([1, 2, 3, 4, 5])))  # Output: (5,)
print(np.shape(np.array([[1, 2, 3], [4, 5, 6]])))  # Output: (2, 3)
print(np.shape(np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])))  # Output: (2, 2, 2)

# --- Size (np.size) ---Total number of elements
print(np.size(np.array([1, 2, 3, 4, 5])))  # Output: 5
print(np.size(np.array([[1, 2, 3], [4, 5, 6]])))  # Output: 6
print(np.size(np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])))  # Output: 8

# --- Itemsize (Attribute Only) ---
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(a.itemsize)  # Output: 8 (or 4 depending on OS) Size of each element in bytes
print(b.itemsize)  # Output: 8
print(c.itemsize)  # Output: 8

# --- Data Type (Attribute Only) ---
print(a.dtype)  # Output: int64 (or int32)