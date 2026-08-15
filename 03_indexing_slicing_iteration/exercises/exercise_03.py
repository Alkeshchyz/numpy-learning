import numpy as np

# Define a 3D NumPy array with shape (2, 2, 3)
data = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])

# 1. Extract the first element (matrix 0, row 0, column 0)
print("The first element:", data[0, 0, 0])

# 2. Extract the element 60 (matrix 0, row 1, column 2)
print("The element 60:", data[0, 1, 2])

# 3. Extract the element 100 (matrix 1, row 1, column 0)
print("The element 100:", data[1, 1, 0])

# 4. Extract the last element using negative indexing
print("The last element:", data[-1, -1, -1])

# 5. Extract the second row of the first matrix (matrix 0, row index 1)
print("The second row of the first array:", data[0, 1])

# 6. Iterate through every element element-by-element using np.nditer()
print("Every element using np.nditer():")
for element in np.nditer(data):
    print(element, end=" ")