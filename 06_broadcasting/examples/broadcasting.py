import numpy as np

# ==========================================
# Step 1: Basic Broadcasting & 2D Addition
# ==========================================
print("=== Step 1: Basic Broadcasting ===")

# 1. Scalar Broadcasting
marks_1d = np.array([70, 80, 90, 60, 75])
bonus_scalar = 5
result_scalar = marks_1d + bonus_scalar

print("Original marks:")
print(marks_1d)
print("\nBonus:")
print(bonus_scalar)
print("\nMarks after bonus:")
print(result_scalar)

# 2. Broadcasting with Two Same-Shape Arrays
prices = np.array([100, 200, 300, 400, 500])
discount = np.array([10, 20, 30, 40, 50])
final_prices = prices - discount

print("\nOriginal prices:")
print(prices)
print("\nDiscount:")
print(discount)
print("\nFinal prices:")
print(final_prices)

# 3. 2D Array + 1D Array Broadcasting
marks_2d = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 88]
])
bonus_row = np.array([5, 10, 15])
updated_marks = marks_2d + bonus_row

print("\nOriginal marks (2D):")
print(marks_2d)
print("\nBonus:")
print(bonus_row)
print("\nUpdated marks:")
print(updated_marks)
print("\n" + "="*40 + "\n")

# ==========================================
# Step 2: Broadcasting with Different Shapes
# ==========================================
print("=== Step 2: Shape Variations ===")

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

column = np.array([
    [1],
    [2],
    [3]
])

print("Original matrix:")
print(matrix)
print("\nColumn:")
print(column)
print("\nResult (matrix + column):")
print(matrix + column)

# Task 1: Multiply every row by column values (3, 1)
values_col = np.array([
    [2],
    [3],
    [4]
])
print("\nTask 1 (matrix * column values):")
print(matrix * values_col)

# Task 2: Add row values (3,) to each column
values_row = np.array([100, 200, 300])
print("\nTask 2 (matrix + row values):")
print(matrix + values_row)

# Task 3: Incompatible Shape Experiment
print("\nTask 3 (Incompatible Shapes Experiment):")
try:
    print(matrix + np.array([1, 2]))
except ValueError as e:
    print(f"ValueError caught: {e}")
print("\n" + "="*40 + "\n")

# ==========================================
# Step 3: Broadcasting Rules & Mini-Task
# ==========================================
print("=== Step 3: Rules & Mini-Task ===")

# Compatible example
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b = np.array([10, 20, 30])

print("A shape:", a.shape)
print("B shape:", b.shape)
print("\nA + B:")
print(a + b)

# Incompatible example
c = np.array([10, 20])
print("\nC shape:", c.shape)
try:
    print(a + c)
except ValueError as e:
    print(f"ValueError caught for A + C: {e}")

# Final Mini-Task
x = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
y = np.array([1, 2, 3])

print("\nx shape:", x.shape)
print("y shape:", y.shape)

print("\nx + y:")
print(x + y)

print("\nx - y:")
print(x - y)

print("\nx * y:")
print(x * y)

print("\nx / y:")
print(x / y)