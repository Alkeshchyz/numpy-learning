import numpy as np

marks = np.array([45, 78, 92, 67, 88, 34, 95, 73, 81, 59])

print("Marks:")
print(marks)

print("\nHighest mark:")
print(np.max(marks))

print("\nIndex of highest mark:")
print(np.argmax(marks))

print("\nLowest mark:")
print(np.min(marks))

print("\nIndex of lowest mark:")
print(np.argmin(marks))