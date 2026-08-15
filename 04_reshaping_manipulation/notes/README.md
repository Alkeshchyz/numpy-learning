================================================================================
                     MATRIX MANIPULATOR – NUMPY PROJECT
        Reshaping & Array Manipulation (Section 04)
================================================================================

OVERVIEW
--------
Matrix Manipulator is a beginner-friendly NumPy project that combines array
reshaping and manipulation techniques learned in Section 04 — Reshaping & Array
Manipulation. The program takes a one‑dimensional array and transforms it into
different shapes and representations, demonstrating key NumPy functions.

OBJECTIVE
---------
The goal of this project is to practice transforming a NumPy array into
different shapes and representations using:

    • reshape()
    • transpose() / .T
    • flatten()
    • ravel()
    • expand_dims()

WHAT THE PROJECT DOES
---------------------
The program starts with a NumPy array containing numbers from 1 to 12:

    np.arange(1, 13)   →   [ 1  2  3  4  5  6  7  8  9 10 11 12 ]

It then performs the following sequence of transformations:

     Original 1D Array
           │
           ▼
        reshape()
           │
           ▼
       3 × 4 Matrix
           │
           ▼
       transpose()
           │
           ▼
       4 × 3 Matrix
           │
           ▼
        flatten()
           │
           ▼
         1D Array
           │
           ▼
         ravel()
           │
           ▼
         1D Array
           │
           ▼
      expand_dims()
           │
           ▼
     Row Array / Column Array

Each step is printed with its resulting shape and contents, allowing the user to
observe the effect of each operation.

NUMPY CONCEPTS USED
-------------------
1. reshape()
   Converts the original 1D array into a 2D matrix of desired dimensions.
   Example: matrix = original.reshape(3, 4)

2. transpose() / .T
   Switches rows and columns of a 2D array.
   Example: transposed = matrix.T   (or np.transpose(matrix))

3. flatten()
   Converts a multidimensional array into a 1D array (returns a copy).
   Example: flat = matrix.flatten()

4. ravel()
   Converts a multidimensional array into a 1D array (returns a view if possible).
   Example: raveled = np.ravel(matrix)

5. expand_dims()
   Adds a new axis/dimension at the specified position.
   Example:
       row_array = np.expand_dims(raveled, axis=0)   # shape (1, n)
       col_array = np.expand_dims(raveled, axis=1)   # shape (n, 1)

6. .shape
   Used to check and print the dimensions of the array at each step.

EXAMPLE DATA AND OUTPUT
-----------------------
Initial array:
    [ 1  2  3  4  5  6  7  8  9 10 11 12 ]

After reshape(3, 4):
    [[ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]]
    Shape: (3, 4)

After transpose (T):
    [[ 1  5  9]
     [ 2  6 10]
     [ 3  7 11]
     [ 4  8 12]]
    Shape: (4, 3)

After flatten():
    [ 1  2  3  4  5  6  7  8  9 10 11 12]
    Shape: (12,)

After ravel():
    [ 1  2  3  4  5  6  7  8  9 10 11 12]
    Shape: (12,)

After expand_dims (axis=0):
    [[ 1  2  3  4  5  6  7  8  9 10 11 12]]
    Shape: (1, 12)

After expand_dims (axis=1):
    [[ 1]
     [ 2]
     [ 3]
     [ 4]
     [ 5]
     [ 6]
     [ 7]
     [ 8]
     [ 9]
     [10]
     [11]
     [12]]
    Shape: (12, 1)

PROJECT STRUCTURE
-----------------
matrix_manipulator/
├── main.py
└── README.md

The main.py file contains the complete code that performs all transformations
with print statements to show each step. The README.md provides an overview of
the project, its purpose, and instructions.

HOW TO RUN
----------
1. Ensure NumPy is installed:
       pip install numpy

2. Navigate to the project directory and run:
       python main.py

3. Observe the printed output showing each transformation and its shape.

LEARNING OUTCOME
----------------
After completing this project, I have practiced:

    • Changing array shapes with reshape()
    • Transposing matrices using .T
    • Converting multidimensional arrays to 1D with flatten() and ravel()
    • Adding new dimensions with expand_dims()
    • Checking array shapes using .shape
    • Combining multiple NumPy operations in a single program
    • Understanding the difference between flatten() (copy) and ravel() (view)

STATUS
------
✅ Completed

================================================================================
                              QUICK REFERENCE
================================================================================

Function / Attribute        | Description
----------------------------+---------------------------------------------------
reshape(new_shape)          | Returns a new array with the specified shape.
.T / transpose()            | Returns the transpose of the array.
flatten()                   | Returns a flattened 1D copy of the array.
ravel()                     | Returns a flattened 1D view (when possible).
expand_dims(arr, axis)      | Inserts a new axis at the given position.
.shape                      | Returns the dimensions of the array.

================================================================================
End of Document
================================================================================