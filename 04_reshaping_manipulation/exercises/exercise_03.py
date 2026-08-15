import numpy as np

# Define original array (shape: 2, 3)
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# 1. Print original array
print("Original Array:")
print(numbers)
print("Shape:", numbers.shape)
print()

# 2. Convert to 1D using np.ravel()
raveled = np.ravel(numbers)
print("Raveled Array:")
print(raveled)
print("Raveled Shape:", raveled.shape)
print()

# 3. Add new axis at position 0 using np.expand_dims()
expanded_axis0 = np.expand_dims(numbers, axis=0)
print("Expanded Dims (axis=0):")
print(expanded_axis0)
print("Shape:", expanded_axis0.shape)
print()

# 4. Add new axis at position 1 using np.expand_dims()
expanded_axis1 = np.expand_dims(numbers, axis=1)
print("Expanded Dims (axis=1):")
print(expanded_axis1)
print("Shape:", expanded_axis1.shape)