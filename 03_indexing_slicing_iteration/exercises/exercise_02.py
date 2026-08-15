import numpy as np

# Define a 3x4 2D NumPy array
matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

# 1. Extract the second row (row index 1)
print("Second row:", matrix[1])

# 2. Extract the third column (all rows ':', column index 2)
print("Third column:", matrix[:, 2])

# 3. Extract element 70 (row index 1, column index 2)
print("Element 70:", matrix[1, 2])

# 4. Extract element 100 (row index 2, column index 1)
print("Element 100:", matrix[2, 1])

# 5. Slice the first two rows (rows index 0 up to, but excluding, index 2)
print("First two rows:\n", matrix[:2])

# 6. Slice the last two columns (all rows, columns from index -2 to end)
print("Last two columns:\n", matrix[:, -2:])

# 7. Reverse the order of rows (step of -1 on the row axis)
print("Matrix in reverse row order:\n", matrix[::-1])