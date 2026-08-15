import numpy as np

numbers = np.array([10, 20, 30, 40])

print("Original array:")
print(numbers)

updated = np.append(numbers, 50)

print("\nAfter appending 50:")
print(updated)

updated = np.append(updated, [60, 70])

print("\nAfter appending 60 and 70:")
print(updated)

print("\nOriginal array:")
print(numbers)