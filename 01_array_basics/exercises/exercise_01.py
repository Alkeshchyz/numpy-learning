import numpy as np

a = np.array([45, 78, 92, 67, 88, 34, 95, 73, 81, 59])

print(a)  # [45 78 92 67 88 34 95 73 81 59]
print(a.ndim)  # 1
print(a.shape)  # (10,)
print(a.size)  # 10
print(a.itemsize)  # 8 (bytes per element)
print(a.dtype)  # int64