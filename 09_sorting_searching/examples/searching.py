import numpy as np

# Step 3 Example Dataset
marks_example = np.array([20, 40, 60, 80, 100])
print("Example Marks:")
print(marks_example)

print("\nPosition to insert 70:")
print(np.searchsorted(marks_example, 70))

print("Position to insert 50:")
print(np.searchsorted(marks_example, 50))

# Multiple values example
values_example = np.array([10, 50, 90])
print("\nValues:", values_example)
print("Insertion positions:", np.searchsorted(marks_example, values_example))

print("\n" + "=" * 40 + "\n")

# ⭐ Mini-task
marks = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
values = np.array([15, 25, 55, 75, 95])

positions = np.searchsorted(marks, values)

print("Sorted Marks Array:")
print(marks)

print("\nValues to Insert:")
print(values)

print("\nInsertion Positions:")
print(positions)