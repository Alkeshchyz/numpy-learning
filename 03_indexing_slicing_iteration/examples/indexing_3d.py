import numpy as np

array_3d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("Shape:", array_3d.shape)

print("First element:", array_3d[0, 0, 0])
print("Element 6:", array_3d[0, 1, 2])
print("Element 10:", array_3d[1, 1, 0])

print("Last element:", array_3d[-1, -1, -1])
print("Element 3:", array_3d[0, 0, 2])
print("Element 8:", array_3d[1, 0, 1])
print("Element 12:", array_3d[1, 1, 2])