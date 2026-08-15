================================================================================
        NumPy Indexing, Slicing & Iteration – Comprehensive Guide
================================================================================

This document covers how to access, select, and iterate through elements of
NumPy arrays. It includes detailed explanations, examples, exercises, and a
complete project to reinforce the concepts.

--------------------------------------------------------------------------------
1. INDEXING
--------------------------------------------------------------------------------

Indexing is used to access individual elements of an array. Python uses
zero‑based indexing: the first element has index 0.

1.1 1D Indexing
----------------
  Example:
    import numpy as np
    numbers = np.array([10, 20, 30, 40, 50])

    print(numbers[0])   # 10
    print(numbers[2])   # 30
    print(numbers[-1])  # 50 (negative indexing)

  Positive indexing:
    Index:   0   1   2   3   4
    Value:  10  20  30  40  50

  Negative indexing:
    Index:  -5  -4  -3  -2  -1
    Value:  10  20  30  40  50

1.2 2D Indexing
----------------
  For a 2D array, indexing follows:  array[row, column]

  Example:
    matrix = np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ])

    print(matrix[0, 0])   # 10
    print(matrix[1, 2])   # 60
    print(matrix[-1, -1]) # 90

1.3 3D Indexing
----------------
  For a 3D array, indexing follows:  array[array_index, row, column]

  Example:
    data = np.array([
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [7, 8, 9],
            [10, 11, 12]
        ]
    ])

    print(data[0, 0, 0])   # 1
    print(data[1, 1, 0])   # 10

  The three indexes represent:  array → row → column.

--------------------------------------------------------------------------------
2. SLICING
--------------------------------------------------------------------------------

Slicing is used to select a range of elements. The general syntax is:

    array[start:stop:step]

  * start is inclusive, stop is exclusive.
  * All parameters are optional.

2.1 1D Slicing
---------------
  Example:
    numbers = np.array([10, 20, 30, 40, 50, 60])
    print(numbers[1:4])   # [20 30 40]

  Step:
    print(numbers[::2])   # every second element → [10 30 50]

  Reverse:
    print(numbers[::-1])  # reverses the array → [60 50 40 30 20 10]

2.2 2D Slicing
---------------
  Matrix:
    matrix = np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ])

  Select rows:
    matrix[0:2]           # first two rows

  Select a column:
    matrix[:, 1]          # second column → [20 50 80]

  Select a section (rows 0-1, columns 1-2):
    matrix[0:2, 1:3]      # [[20 30] [50 60]]

--------------------------------------------------------------------------------
3. ITERATION
--------------------------------------------------------------------------------

Iteration allows us to go through array elements one by one.

3.1 1D Array
-------------
  numbers = np.array([10, 20, 30, 40])
  for number in numbers:
      print(number)

3.2 2D Array
-------------
  matrix = np.array([
      [10, 20, 30],
      [40, 50, 60]
  ])

  for row in matrix:
      print(row)          # each row is printed as a 1D array

  A normal loop over a 2D array returns each row.

3.3 np.nditer()
----------------
  np.nditer() can be used to iterate through individual elements of a
  multidimensional array.

  for value in np.nditer(matrix):
      print(value)        # prints 10, 20, 30, 40, 50, 60 (one per line)

--------------------------------------------------------------------------------
4. QUICK REFERENCE
--------------------------------------------------------------------------------

  Concept                    | Example
  ---------------------------+-----------------------------
  1D indexing                | array[2]
  Negative indexing          | array[-1]
  2D indexing                | array[1, 2]
  3D indexing                | array[1, 0, 2]
  Slicing                    | array[1:4]
  Step                       | array[::2]
  Reverse                    | array[::-1]
  2D column                  | array[:, 1]
  Iteration                  | for x in array
  Individual element iter.   | np.nditer(array)

--------------------------------------------------------------------------------
5. EXERCISES
--------------------------------------------------------------------------------

The following exercises reinforce the concepts of indexing, slicing, and
iteration. All exercises are completed.

5.1 Exercise 01 – Array Element Selector
----------------------------------------
  Objective:
    Practice accessing elements and selecting ranges from a 1D NumPy array.

  Concepts Practiced:
    • Positive indexing
    • Negative indexing
    • Basic slicing
    • Step slicing

  File: exercise_01.py
  Status: ✅ Completed

5.2 Exercise 02 – 2D Indexing & Slicing
----------------------------------------
  Objective:
    Practice accessing rows, columns, individual elements, and sections of a
    2D array.

  Concepts Practiced:
    • 2D indexing
    • Row selection
    • Column selection
    • 2D slicing

  File: exercise_02.py
  Status: ✅ Completed

5.3 Exercise 03 – 3D Indexing & Iteration
------------------------------------------
  Objective:
    Practice accessing elements from a 3D array and iterating through all of
    its elements.

  Concepts Practiced:
    • 3D indexing
    • 3D slicing
    • np.nditer()
    • Multidimensional iteration

  File: exercise_03.py
  Status: ✅ Completed

--------------------------------------------------------------------------------
6. PROJECT – STUDENT DATA SELECTOR
--------------------------------------------------------------------------------

A beginner‑friendly NumPy project that applies indexing, slicing, and iteration
to a simple student dataset.

6.1 Objective
--------------
  To demonstrate how specific rows, columns, and elements can be selected from a
  NumPy array using the concepts learned in this section.

6.2 Dataset
------------
  students = np.array([
      [101, 78, 85, 92],
      [102, 65, 70, 75],
      [103, 88, 91, 95],
      [104, 55, 60, 68],
      [105, 90, 87, 93]
  ])

  Columns:
    Column 0 : Student ID
    Column 1 : Subject 1 marks
    Column 2 : Subject 2 marks
    Column 3 : Subject 3 marks

6.3 Features
-------------
  The program demonstrates:
    • Selecting all student IDs
    • Selecting marks of a specific student
    • Selecting the first and last student
    • Selecting a specific subject
    • Selecting multiple students using slicing
    • Selecting only marks while excluding student IDs
    • Iterating through every value

6.4 NumPy Concepts Used
------------------------
  Indexing:
    students[0]
    students[-1]
    students[1, 2]

  Slicing:
    students[:3]
    students[-2:]
    students[:, 1:]

  Iteration:
    for value in np.nditer(students):
        print(value)

6.5 Project Structure
----------------------
  student_data_selector/
  ├── main.py
  └── README.md

6.6 Example Output
-------------------
  Student Data:
  [[101  78  85  92]
   [102  65  70  75]
   [103  88  91  95]
   [104  55  60  68]
   [105  90  87  93]]

  Student IDs: ...
  First Student Marks: ...
  Last Student Marks: ...
  Subject 2 Marks: ...

6.7 Learning Outcome
---------------------
  Through this project, I practiced using NumPy indexing and slicing to select
  specific parts of structured numerical data, and iterating through
  multidimensional arrays using np.nditer().

  Status: ✅ Completed

--------------------------------------------------------------------------------
7. FINAL STATUS
--------------------------------------------------------------------------------

  Section 03 – NumPy Indexing, Slicing & Iteration  : ✅ Completed
  Exercises (01, 02, 03)                           : ✅ Completed
  Project – Student Data Selector                  : ✅ Completed

================================================================================
End of Document
================================================================================