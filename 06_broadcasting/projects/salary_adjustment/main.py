import numpy as np

# Step 1 — Employee salaries
salaries = np.array([
    [30000, 35000, 40000],
    [45000, 50000, 55000],
    [60000, 65000, 70000]
])

print("Original Salaries:")
print(salaries)

# Step 2 — Apply a common bonus (Scalar Broadcasting)
bonus = 5000
updated_salaries = salaries + bonus

print("\nSalaries after common bonus:")
print(updated_salaries)

# Step 3 — Different adjustment for each column (Shape: 3,)
adjustment = np.array([2000, 3000, 5000])
adjusted_salaries = salaries + adjustment

print("\nSalaries after column-wise adjustment:")
print(adjusted_salaries)

# Step 4 — Different adjustment for each row (Shape: 3, 1)
row_bonus = np.array([
    [1000],
    [2000],
    [3000]
])
row_adjusted = salaries + row_bonus

print("\nSalaries after row-wise adjustment:")
print(row_adjusted)

# Step 5 — Percentage adjustment
percentage = np.array([1.05, 1.10, 1.15])
final_salaries = salaries * percentage

print("\nFinal salaries:")
print(final_salaries)

# Step 6 — Display shapes
print("\nShapes:")
print("Salaries:", salaries.shape)
print("Adjustment:", adjustment.shape)
print("Row Bonus:", row_bonus.shape)
print("Percentage:", percentage.shape)