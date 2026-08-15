import numpy as np


# Students enrolled in Python.
python = np.array([
    101, 102, 103, 104, 105
])

# Students enrolled in Java.
java = np.array([
    104, 105, 106, 107, 108
])


# TODO:
# 1. Find students enrolled in either course.
# 2. Find students enrolled in both courses.
# 3. Find students enrolled only in Python.
# 4. Find students enrolled only in Java.
#
# Use:
# np.union1d()
# np.intersect1d()
# np.setdiff1d()
import numpy as np

# Students enrolled in Python
python = np.array([101, 102, 103, 104, 105])

# Students enrolled in Java
java = np.array([104, 105, 106, 107, 108])

# 1. Find students enrolled in either course (Union)
either_course = np.union1d(python, java)

# 2. Find students enrolled in both courses (Intersection)
both_courses = np.intersect1d(python, java)

# 3. Find students enrolled only in Python (Set Difference: python - java)
only_python = np.setdiff1d(python, java)

# 4. Find students enrolled only in Java (Set Difference: java - python)
only_java = np.setdiff1d(java, python)

# Display results
print("1. Students in either course (Union):")
print(either_course)

print("\n2. Students in both courses (Intersection):")
print(both_courses)

print("\n3. Students enrolled ONLY in Python:")
print(only_python)

print("\n4. Students enrolled ONLY in Java:")
print(only_java)