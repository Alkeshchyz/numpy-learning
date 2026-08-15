import numpy as np


# ---------------------------------------------------------
# Dataset
# ---------------------------------------------------------

# Students who completed the Python course.
python_students = np.array([
    101, 102, 103, 104, 105, 106
])

# Students who completed the NumPy course.
numpy_students = np.array([
    103, 104, 105, 106, 107, 108
])

# Students who completed the Pandas course.
pandas_students = np.array([
    105, 106, 107, 108, 109, 110
])


# ---------------------------------------------------------
# Display original datasets
# ---------------------------------------------------------

print("========== COURSE DATA ==========")

print("Python students:")
print(python_students)

print("\nNumPy students:")
print(numpy_students)

print("\nPandas students:")
print(pandas_students)


# ---------------------------------------------------------
# Python + NumPy
# ---------------------------------------------------------

print("\n========== PYTHON & NUMPY ==========")

# Students who completed at least one of the courses.
python_numpy_union = np.union1d(
    python_students,
    numpy_students
)

print("Students in Python OR NumPy:")
print(python_numpy_union)


# Students who completed both courses.
python_numpy_intersection = np.intersect1d(
    python_students,
    numpy_students
)

print("\nStudents in Python AND NumPy:")
print(python_numpy_intersection)


# Students who completed Python but not NumPy.
python_only = np.setdiff1d(
    python_students,
    numpy_students
)

print("\nPython only:")
print(python_only)


# Students who completed NumPy but not Python.
numpy_only = np.setdiff1d(
    numpy_students,
    python_students
)

print("\nNumPy only:")
print(numpy_only)


# Students who completed exactly one of the two courses.
python_numpy_exclusive = np.setxor1d(
    python_students,
    numpy_students
)

print("\nExactly one of Python or NumPy:")
print(python_numpy_exclusive)


# ---------------------------------------------------------
# All Three Courses
# ---------------------------------------------------------

print("\n========== ALL THREE COURSES ==========")

# Students who completed both Python and NumPy.
python_numpy = np.intersect1d(
    python_students,
    numpy_students
)

# Find students who also completed Pandas.
all_three = np.intersect1d(
    python_numpy,
    pandas_students
)

print("Students who completed all three:")
print(all_three)


# ---------------------------------------------------------
# Students in at least one course
# ---------------------------------------------------------

all_students = np.union1d(
    np.union1d(
        python_students,
        numpy_students
    ),
    pandas_students
)

print("\nStudents in at least one course:")
print(all_students)


# ---------------------------------------------------------
# Students who completed only Pandas
# ---------------------------------------------------------

pandas_only = np.setdiff1d(
    pandas_students,
    np.union1d(
        python_students,
        numpy_students
    )
)

print("\nPandas only:")
print(pandas_only)


# ---------------------------------------------------------
# Final Statistics
# ---------------------------------------------------------

print("\n========== SUMMARY ==========")

print("Total unique students:")
print(all_students.size)

print("\nStudents in all three courses:")
print(all_three.size)

print("\nPython only:")
print(python_only.size)

print("\nNumPy only:")
print(numpy_only.size)

print("\nPandas only:")
print(pandas_only.size)