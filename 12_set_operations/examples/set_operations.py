import numpy as np


# ---------------------------------------------------------
# Example datasets
# ---------------------------------------------------------

# Students who completed Python training.
python_students = np.array([
    101, 102, 103, 104, 105
])

# Students who completed NumPy training.
numpy_students = np.array([
    103, 104, 105, 106, 107
])

print("Python students:")
print(python_students)

print("\nNumPy students:")
print(numpy_students)


# ---------------------------------------------------------
# UNION
# ---------------------------------------------------------

# np.union1d() returns all unique values
# present in either of the two arrays.
union = np.union1d(
    python_students,
    numpy_students
)

print("\nUnion:")
print(union)


# ---------------------------------------------------------
# INTERSECTION
# ---------------------------------------------------------

# np.intersect1d() returns values that
# exist in BOTH arrays.
intersection = np.intersect1d(
    python_students,
    numpy_students
)

print("\nIntersection:")
print(intersection)


# ---------------------------------------------------------
# SET DIFFERENCE
# ---------------------------------------------------------

# np.setdiff1d() returns values that exist
# in the first array but NOT in the second.
python_only = np.setdiff1d(
    python_students,
    numpy_students
)

print("\nPython only:")
print(python_only)


numpy_only = np.setdiff1d(
    numpy_students,
    python_students
)

print("\nNumPy only:")
print(numpy_only)


# ---------------------------------------------------------
# SYMMETRIC DIFFERENCE
# ---------------------------------------------------------

# np.setxor1d() returns values that exist
# in either array, but NOT in both.
symmetric_difference = np.setxor1d(
    python_students,
    numpy_students
)

print("\nSymmetric difference:")
print(symmetric_difference)


# ---------------------------------------------------------
# UNIQUE VALUES
# ---------------------------------------------------------

# np.unique() removes duplicate values.
all_students = np.array([
    101, 102, 103, 103, 104,
    105, 105, 106, 107
])

unique_students = np.unique(all_students)

print("\nOriginal student IDs:")
print(all_students)

print("\nUnique student IDs:")
print(unique_students)