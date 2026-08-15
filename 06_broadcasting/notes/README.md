================================================================================
                          SALARY ADJUSTMENT
               NumPy Broadcasting Project (Section 06)
================================================================================

OVERVIEW
--------
Salary Adjustment is a practical NumPy project that demonstrates broadcasting by
applying bonuses, salary adjustments, and percentage increases to employee
salaries. The program shows how NumPy can perform operations on arrays of
different shapes without manually repeating values.

================================================================================
PROJECT OBJECTIVE
================================================================================

The objective of this project is to understand how NumPy broadcasting can be
used to perform calculations on multidimensional arrays without manually
repeating values.

The project demonstrates:
  • Scalar broadcasting
  • Column-wise broadcasting
  • Row-wise broadcasting
  • Percentage-based adjustments
  • Working with arrays of different but compatible shapes
  • Understanding NumPy array shapes (.shape)

================================================================================
DATASET
================================================================================

The project uses a 3 × 3 salary matrix:

    import numpy as np

    salaries = np.array([
        [30000, 35000, 40000],
        [45000, 50000, 55000],
        [60000, 65000, 70000]
    ])

The array has the shape (3, 3).
For this project, the rows and columns represent different groups of employees
or salary categories.

================================================================================
BROADCASTING OPERATIONS
================================================================================

1. Scalar Broadcasting
----------------------
A common bonus of 5000 is added to every salary:

    bonus = 5000
    updated_salaries = salaries + bonus

NumPy automatically broadcasts the scalar value:

    [30000 35000 40000]    [5000 5000 5000]
    [45000 50000 55000] +  [5000 5000 5000]
    [60000 65000 70000]    [5000 5000 5000]

Result:

    [[35000 40000 45000]
     [50000 55000 60000]
     [65000 70000 75000]]

No manually created 3 × 3 bonus array is required.

2. Column-wise Broadcasting
---------------------------
Different adjustments are applied to each column:

    adjustment = np.array([2000, 3000, 5000])
    adjusted_salaries = salaries + adjustment

Shapes:
    salaries   → (3, 3)
    adjustment → (3,)

NumPy broadcasts the adjustment across every row:

                 2000   3000   5000
                   ↓      ↓      ↓
    30000        35000  38000  45000
    45000        47000  53000  60000
    60000        62000  68000  75000

3. Row-wise Broadcasting
------------------------
Different bonuses are applied to each row:

    row_bonus = np.array([
        [1000],
        [2000],
        [3000]
    ])

    row_adjusted = salaries + row_bonus

Shapes:
    salaries  → (3, 3)
    row_bonus → (3, 1)

The single value in each row is broadcast across all columns:

    [30000 35000 40000] + 1000
    [45000 50000 55000] + 2000
    [60000 65000 70000] + 3000

Result:

    [[31000 36000 41000]
     [47000 52000 57000]
     [63000 68000 73000]]

4. Percentage-Based Adjustment
-------------------------------
Different percentage increases are applied to each column:

    percentage = np.array([1.05, 1.10, 1.15])
    final_salaries = salaries * percentage

The values represent:
    1.05 → 5% increase
    1.10 → 10% increase
    1.15 → 15% increase

Shapes:
    salaries   → (3, 3)
    percentage → (3,)

NumPy applies the corresponding percentage to every row.

For example:
    30000 × 1.05 = 31500
    35000 × 1.10 = 38500
    40000 × 1.15 = 46000

5. Understanding Shapes
-----------------------
The project prints the shapes of the arrays:

    print("Salaries:", salaries.shape)
    print("Adjustment:", adjustment.shape)
    print("Row Bonus:", row_bonus.shape)
    print("Percentage:", percentage.shape)

Expected output:

    Salaries: (3, 3)
    Adjustment: (3,)
    Row Bonus: (3, 1)
    Percentage: (3,)

Understanding shapes is important when working with broadcasting because NumPy
must determine whether two arrays have compatible dimensions.

================================================================================
BROADCASTING CONCEPTS DEMONSTRATED
================================================================================

+---------------------------+-------------+-------------+-------------------+
| Operation                 | First Shape | Second Shape| Broadcasting      |
+---------------------------+-------------+-------------+-------------------+
| salaries + 5000           | (3, 3)      | scalar      | ✅               |
| salaries + adjustment     | (3, 3)      | (3,)        | ✅               |
| salaries + row_bonus      | (3, 3)      | (3, 1)      | ✅               |
| salaries * percentage     | (3, 3)      | (3,)        | ✅               |
+---------------------------+-------------+-------------+-------------------+

================================================================================
WHAT I LEARNED
================================================================================

Through this project, I practiced:

  • Creating multidimensional NumPy arrays
  • Understanding .shape
  • Adding a scalar to an array
  • Broadcasting a 1D array across rows
  • Broadcasting a column vector across columns
  • Performing percentage calculations with NumPy
  • Working with compatible array shapes
  • Applying the same operation to large amounts of data efficiently

================================================================================
TECHNOLOGIES USED
================================================================================

  • Python
  • NumPy

================================================================================
PROJECT STRUCTURE
================================================================================

    salary_adjustment/
    ├── main.py
    └── README.md

  main.py    – Contains the complete salary adjustment program.
  README.md  – Contains project documentation, concepts, examples, and
               learning outcomes.

================================================================================
HOW TO RUN
================================================================================

1. Make sure NumPy is installed:

    pip install numpy

2. Run the program from the project directory:

    python main.py

================================================================================
EXAMPLE OUTPUT
================================================================================

Original Salaries:
[[30000 35000 40000]
 [45000 50000 55000]
 [60000 65000 70000]]

Salaries after common bonus:
[[35000 40000 45000]
 [50000 55000 60000]
 [65000 70000 75000]]

Salaries after column-wise adjustment:
[[32000 38000 45000]
 [47000 53000 60000]
 [62000 68000 75000]]

Salaries after row-wise adjustment:
[[31000 36000 41000]
 [47000 52000 57000]
 [63000 68000 73000]]

Final percentage-adjusted salaries:
[[31500 38500 46000]
 [47250 55000 63250]
 [63000 71500 80500]]

Array Shapes:
Salaries: (3, 3)
Adjustment: (3,)
Row Bonus: (3, 1)
Percentage: (3,)

================================================================================
KEY TAKEAWAY
================================================================================

The main idea of this project is that NumPy broadcasting allows arrays with
compatible shapes to work together without manually expanding or copying data.

This makes numerical operations shorter, cleaner, and more efficient.

================================================================================
QUICK REFERENCE
================================================================================

Function / Concept          | Description
----------------------------+---------------------------------------------------
arr + scalar                | Adds scalar to every element
arr + 1D_array              | Broadcasts 1D array across rows
arr + column_vector         | Broadcasts column vector across columns
arr * percentage_array      | Applies percentages element-wise
.shape                      | Returns dimensions of the array
Broadcasting                | NumPy's ability to operate on arrays of different shapes

================================================================================
STATUS
================================================================================

  Status       : ✅ Completed
  Section      : 06 — Broadcasting
  Project      : Salary Adjustment
  Library      : NumPy

================================================================================
End of Document
================================================================================