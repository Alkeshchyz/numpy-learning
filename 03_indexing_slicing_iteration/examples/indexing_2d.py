import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("First row:", matrix[0])
print("Second row:", matrix[1])

print("Element at row 1, column 2:", matrix[1, 2])
print("First element:", matrix[0, 0])
print("Last element:", matrix[-1, -1])
print("20:", matrix[0, 1])
print("60:", matrix[1, 2])
print("80:", matrix[2, 1])