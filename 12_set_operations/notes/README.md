================================================================================
               SECTION 12 — SET OPERATIONS WITH NUMPY
================================================================================

OVERVIEW
--------
This section covers NumPy's set operations for comparing and analyzing arrays.
These operations are especially useful when working with:
  • Student IDs
  • Course enrollment
  • User lists
  • Product lists
  • Database records
  • Membership data

================================================================================
NUMPY SET OPERATIONS – REFERENCE
================================================================================

1. np.union1d()
----------------
Returns all unique values found in either array.

Syntax:
    np.union1d(a, b)

Example:
    A = [1, 2, 3]
    B = [3, 4, 5]
    Union: [1, 2, 3, 4, 5]

2. np.intersect1d()
--------------------
Returns values present in both arrays.

Syntax:
    np.intersect1d(a, b)

Example:
    A = [1, 2, 3]
    B = [2, 3, 4]
    Intersection: [2, 3]

3. np.setdiff1d()
------------------
Returns values that exist in the first array but not the second.

Syntax:
    np.setdiff1d(a, b)

Example:
    A = [1, 2, 3]
    B = [2, 3, 4]
    Difference (A - B): [1]

Order matters:
    np.setdiff1d(b, a)  → [4]

4. np.setxor1d()
-----------------
Returns values that exist in exactly one of the arrays (symmetric difference).

Syntax:
    np.setxor1d(a, b)

Example:
    A = [1, 2, 3]
    B = [2, 3, 4]
    Symmetric difference: [1, 4]

5. np.unique()
---------------
Removes duplicate values from an array.

Syntax:
    np.unique(array)

Example:
    Original: [1, 2, 2, 3, 3, 3]
    Unique:   [1, 2, 3]

It can also return frequencies:

    unique_values, counts = np.unique(array, return_counts=True)

================================================================================
QUICK REFERENCE TABLE
================================================================================

+---------------------+--------------------------------------------------------+
| Function            | Purpose                                                |
+---------------------+--------------------------------------------------------+
| np.union1d()        | Values in either array                                 |
| np.intersect1d()    | Values in both arrays                                  |
| np.setdiff1d()      | Values only in the first array                         |
| np.setxor1d()       | Values in exactly one array                            |
| np.unique()         | Remove duplicates                                      |
+---------------------+--------------------------------------------------------+

================================================================================
SECTION 12 – EXERCISES
================================================================================

The following exercises reinforce the concepts of set operations.

Exercise 01 – Course Enrollment
-------------------------------
Compare Python and Java student enrollment.

Practice:
    • np.union1d()
    • np.intersect1d()
    • np.setdiff1d()

Tasks:
    1. Students in either course (union)
    2. Students in both courses (intersection)
    3. Python-only students (difference)
    4. Java-only students (difference, reversed)

Exercise 02 – Club Membership
-----------------------------
Compare sports and music club membership.

Practice:
    • Union
    • Intersection
    • Difference
    • Symmetric difference

Tasks:
    1. Students in at least one club (union)
    2. Students in both clubs (intersection)
    3. Sports-only students (difference)
    4. Music-only students (difference)
    5. Students in exactly one club (symmetric difference)

Exercise 03 – Duplicate Data Cleaning
-------------------------------------
Analyze duplicated student IDs.

Practice:
    • np.unique()
    • return_counts
    • array .size

Tasks:
    1. Find unique IDs.
    2. Count unique students.
    3. Calculate duplicate entries (total - unique).

Skills Practiced
-----------------
After completing these exercises, you should be able to:
    • Compare datasets using set operations
    • Find common records
    • Find exclusive records
    • Remove duplicates
    • Analyze membership information
    • Combine multiple set operations

================================================================================
PROJECT – SET COMPARISON
================================================================================

A practical NumPy project for comparing student enrollment across Python,
NumPy, and Pandas courses.

PROJECT OBJECTIVE
-----------------
The goal of this project is to apply NumPy set operations to a realistic
dataset. The project determines:
    • Students enrolled in at least one course
    • Students enrolled in multiple courses
    • Students enrolled in all three courses
    • Students enrolled in only one course
    • Total unique students

DATASET
-------
The project contains three student groups.

Python students:
    python_students = np.array([101, 102, 103, 104, 105, 106])

NumPy students:
    numpy_students = np.array([103, 104, 105, 106, 107, 108])

Pandas students:
    pandas_students = np.array([105, 106, 107, 108, 109, 110])

SET OPERATIONS USED
-------------------
1. Union (np.union1d())
   Finds students enrolled in either of two courses.

2. Intersection (np.intersect1d())
   Finds students enrolled in both courses.

3. Difference (np.setdiff1d())
   Finds students who belong to one group but not another.

4. Symmetric Difference (np.setxor1d())
   Finds students who belong to exactly one of two groups.

STUDENTS IN ALL THREE COURSES
-----------------------------
The project first finds the students shared between Python and NumPy:

    python_numpy = np.intersect1d(python_students, numpy_students)

Then compares that result with Pandas:

    all_three = np.intersect1d(python_numpy, pandas_students)

This demonstrates how multiple set operations can be combined.

STUDENTS IN AT LEAST ONE COURSE
-------------------------------
The project combines all three arrays using repeated union operations:

    all_students = np.union1d(python_students, numpy_students)
    all_students = np.union1d(all_students, pandas_students)

This produces the complete list of unique students.

SUMMARY STATISTICS
------------------
The project calculates:
    • Total unique students
    • Number of students in all three courses
    • Python-only students
    • NumPy-only students
    • Pandas-only students

This turns raw enrollment data into useful information.

CONCEPTS DEMONSTRATED
---------------------
+---------------------+--------------------------------------------------------+
| Function            | Purpose                                                |
+---------------------+--------------------------------------------------------+
| np.union1d()        | Combine unique values                                  |
| np.intersect1d()    | Find common values                                     |
| np.setdiff1d()      | Find exclusive values                                  |
| np.setxor1d()       | Find values in exactly one dataset                     |
| np.unique()         | Remove duplicates                                      |
| .size               | Count array elements                                   |
+---------------------+--------------------------------------------------------+

PROJECT STRUCTURE
-----------------
    set_comparison/
    ├── main.py
    └── README.md

HOW TO RUN
----------
1. Install NumPy:
    pip install numpy

2. Run the program:
    python main.py

EXPECTED OUTPUT (approximate)
-----------------------------
Python Students: [101 102 103 104 105 106]
NumPy Students:  [103 104 105 106 107 108]
Pandas Students: [105 106 107 108 109 110]

Students in at least one course:
[101 102 103 104 105 106 107 108 109 110]
Total unique: 10

Students in all three courses:
[105 106]

Python-only students:
[101 102]

NumPy-only students:
[107 108]

Pandas-only students:
[109 110]

KEY TAKEAWAYS
-------------
This project helped me understand how to:
    • Compare multiple datasets
    • Find common records
    • Find unique records
    • Identify exclusive records
    • Combine multiple set operations
    • Analyze real-world membership data
    • Use NumPy for practical data comparison

FUTURE IMPROVEMENTS
-------------------
Possible improvements:
    • Load student data from CSV files
    • Add student names
    • Add course names dynamically
    • Create an interactive menu
    • Compare more than three courses
    • Generate enrollment reports
    • Visualize course overlap
    • Detect duplicate student records

================================================================================
FINAL STATUS
================================================================================

  Section 12 – Set Operations
    Notes & Examples  : ✅ Completed
    Exercises         : ✅ Completed
    Project (Set Comparison) : ✅ Completed

================================================================================
End of Document
================================================================================