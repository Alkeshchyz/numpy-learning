================================================================================
                         DATA FILTER – NUMPY PROJECT
        Advanced Indexing & Selection (Section 05)
================================================================================

OVERVIEW
--------
Data Filter is a beginner-friendly NumPy project that demonstrates advanced
indexing and selection techniques using a student marks dataset. The program
applies various filtering methods to analyze, classify, and extract meaningful
information from numerical data.

OBJECTIVE
---------
The goal of this project is to practice filtering and analyzing numerical data
using:

    • Boolean indexing
    • np.where()
    • np.max()
    • np.min()
    • np.argmax()
    • np.argmin()
    • Multiple conditions

DATASET
-------
The project uses the following student marks:

    marks = np.array([45, 78, 92, 67, 88, 34, 95, 73, 81, 59])

A mark of 60 or above is considered passing.

PROJECT FEATURES
----------------

1. Passing Students
   Filters all marks greater than or equal to 60.
   Code: marks[marks >= 60]
   Output: [78 92 67 88 95 73 81]

2. Failing Students
   Filters all marks below 60.
   Code: marks[marks < 60]
   Output: [45 34 59]

3. High Performers
   Filters marks greater than or equal to 80.
   Code: marks[marks >= 80]
   Output: [92 88 95 81]

4. Pass/Fail Status
   Uses np.where() to classify each mark as "Pass" or "Fail".
   Code: np.where(marks >= 60, "Pass", "Fail")
   Output: ['Fail' 'Pass' 'Pass' 'Pass' 'Pass' 'Fail' 'Pass' 'Pass' 'Pass' 'Fail']

5. Highest and Lowest Marks
   Uses np.max() and np.min() to find the extremes.
   Code:
       np.max(marks)   → 95
       np.min(marks)   → 34

6. Highest and Lowest Mark Positions
   Uses np.argmax() and np.argmin() to find the indices.
   Code:
       np.argmax(marks)   → 6   (index of mark 95)
       np.argmin(marks)   → 5   (index of mark 34)

7. Marks Between 70 and 90
   Uses multiple Boolean conditions with the & operator.
   Code: marks[(marks >= 70) & (marks <= 90)]
   Output: [78 88 73 81]

NUMPY CONCEPTS USED
-------------------
┌─────────────────────┬────────────────────────────────────────────────────────┐
│ Concept              │ Purpose                                               │
├─────────────────────┼────────────────────────────────────────────────────────┤
│ Boolean Indexing     │ Filter values based on conditions                    │
│ np.where()           │ Select or replace values based on a condition        │
│ np.max()             │ Find the highest value                               │
│ np.min()             │ Find the lowest value                                │
│ np.argmax()          │ Find the index of the highest value                 │
│ np.argmin()          │ Find the index of the lowest value                  │
│ & (ampersand)        │ Combine multiple conditions                         │
└─────────────────────┴────────────────────────────────────────────────────────┘

PROJECT STRUCTURE
-----------------
data_filter/
├── main.py
└── README.md

The main.py file contains the complete code that performs all filtering and
analysis operations with print statements to display each result. The README.md
provides an overview of the project, its purpose, and instructions.

HOW TO RUN
----------
1. Ensure NumPy is installed:
       pip install numpy

2. Navigate to the project directory and run:
       python main.py

3. Observe the printed output showing each filtering and analysis result.

EXAMPLE OUTPUT
--------------
Student Marks:
[45 78 92 67 88 34 95 73 81 59]

Passing Marks (>= 60):
[78 92 67 88 95 73 81]

Failing Marks (< 60):
[45 34 59]

High Performers (>= 80):
[92 88 95 81]

Pass/Fail Status:
['Fail' 'Pass' 'Pass' 'Pass' 'Pass' 'Fail' 'Pass' 'Pass' 'Pass' 'Fail']

Highest Mark: 95
Lowest Mark: 34

Index of Highest Mark: 6
Index of Lowest Mark: 5

Marks Between 70 and 90:
[78 88 73 81]

LEARNING OUTCOME
----------------
Through this project, I practiced:

    • Filtering NumPy arrays using conditions
    • Combining multiple conditions with the & operator
    • Finding specific values (maximum, minimum)
    • Finding the positions of minimum and maximum values using argmax/argmin
    • Classifying data using np.where()
    • Applying multiple NumPy functions to a single dataset
    • Understanding and interpreting filtering results

STATUS
------
✅ Completed

================================================================================
                              QUICK REFERENCE
================================================================================

Function / Technique       | Description
---------------------------+----------------------------------------------------
arr[condition]             | Boolean indexing – returns elements where condition is True
np.where(cond, x, y)       | Returns x where cond is True, y where False
np.max(arr)                | Returns the maximum value in the array
np.min(arr)                | Returns the minimum value in the array
np.argmax(arr)             | Returns the index of the maximum value
np.argmin(arr)             | Returns the index of the minimum value
(cond1) & (cond2)          | Logical AND – combines multiple conditions
(cond1) | (cond2)          | Logical OR – combines multiple conditions
~cond                      | Logical NOT – negates a condition

================================================================================
End of Document
================================================================================