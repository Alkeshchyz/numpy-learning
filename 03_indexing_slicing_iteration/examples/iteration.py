import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

for number in numbers:
    print(number)

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

for row in matrix:
    print(row)

print("Using np.nditer():")

for value in np.nditer(matrix):
    print(value)