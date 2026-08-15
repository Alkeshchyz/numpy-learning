================================================================================
                           ARRAY MANAGER
              NumPy Project – Section 10 (Array Manipulation)
================================================================================

OVERVIEW
--------
Array Manager is a practical NumPy project for adding, combining, removing, and
analyzing numerical arrays. It demonstrates core array manipulation operations
using NumPy's built‑in functions and custom Python functions.

================================================================================
PROJECT OBJECTIVE
================================================================================

The purpose of this project is to apply the concepts learned in Section 10 —
Array Manipulation to a practical program.

The project demonstrates how NumPy can be used to:
  • Add new values to an array
  • Combine multiple arrays
  • Remove values using indices
  • Analyze array dimensions
  • Determine array shape and size
  • Find unique values
  • Count occurrences of values

================================================================================
INITIAL DATASET
================================================================================

The project starts with a NumPy array containing scores:

    import numpy as np

    scores = np.array([78, 85, 92, 78, 88, 95, 85])

The program then modifies and analyzes this data using different NumPy
operations.

================================================================================
PROJECT FUNCTIONS
================================================================================

The project uses several custom functions to organize the operations.

1. add_values()
----------------
    def add_values(data, values):
        return np.append(data, values)

This function adds new values to an existing NumPy array using np.append().

Example:
    Before: [78 85 92]
    Add:    [75 90]
    After:  [78 85 92 75 90]

2. combine_arrays()
-------------------
    def combine_arrays(first, second):
        return np.concatenate((first, second))

This function combines two arrays into a single array using np.concatenate().

Example:
    Array 1: [10 20 30]
    Array 2: [40 50 60]
    Combined: [10 20 30 40 50 60]

3. remove_values()
------------------
    def remove_values(data, indices):
        return np.delete(data, indices)

This function removes values from specific positions using np.delete().

Example:
    Original: [10 20 30 40 50]
    Delete index 2:  [10 20 40 50]

4. array_information()
----------------------
    def array_information(data):
        print("Dimensions:", np.ndim(data))
        print("Shape:", data.shape)
        print("Size:", data.size)

This function provides basic information about the array.

    • Dimensions:  np.ndim(data)   → number of dimensions
    • Shape:       data.shape      → size of each dimension
    • Size:        data.size       → total number of elements

Example for a 2D array:
    Array:  [[1 2 3]
             [4 5 6]]

    Dimensions: 2
    Shape: (2, 3)
    Size: 6

5. show_unique_values()
-----------------------
    def show_unique_values(data):
        unique_values, counts = np.unique(
            data,
            return_counts=True
        )

This function finds unique values and counts how often each value occurs using
np.unique() with return_counts=True.

Example:
    Array: [10 20 10 30 20 10]
    Unique values: [10 20 30]
    Occurrences:   [3  2  1]

================================================================================
PROGRAM WORKFLOW
================================================================================

The project follows this workflow:

    Initial Array
          │
          ▼
    Add New Values
          │
          ▼
    Combine With Another Array
          │
          ▼
    Remove Selected Values
          │
          ▼
    Analyze Array
          ├── Dimensions
          ├── Shape
          └── Size
          │
          ▼
    Find Unique Values
          │
          ▼
    Count Occurrences

================================================================================
NUMY CONCEPTS DEMONSTRATED
================================================================================

+---------------------+--------------------------------------------------------+
| NumPy Concept       | Purpose                                                |
+---------------------+--------------------------------------------------------+
| np.append()         | Add values to the end of an array                      |
| np.concatenate()    | Combine two or more arrays                             |
| np.delete()         | Remove elements by index                               |
| np.ndim()           | Find the number of dimensions                          |
| .shape              | Find the shape of the array                            |
| .size               | Find the total number of elements                      |
| np.unique()         | Find unique values                                     |
| return_counts=True  | Count occurrences of each unique value                 |
| NumPy arrays        | Store and manipulate numerical data                    |
| Custom functions    | Organize reusable operations                           |
+---------------------+--------------------------------------------------------+

================================================================================
PROJECT STRUCTURE
================================================================================

    array_manager/
    ├── main.py
    └── README.md

  main.py    – Contains the complete Array Manager program.
  README.md  – Contains project documentation and explanations of the NumPy
               concepts used.

================================================================================
HOW TO RUN
================================================================================

1. Make sure NumPy is installed:

    pip install numpy

2. Run the program from the project directory:

    python main.py

================================================================================
EXPECTED OUTPUT
================================================================================

Original scores:
[78 85 92 78 88 95 85]

After adding new scores (e.g., [72, 90]):
[78 85 92 78 88 95 85 72 90]

After combining with another array (e.g., [65, 80, 85]):
[78 85 92 78 88 95 85 72 90 65 80 85]

After removing selected values (e.g., indices [2, 5]):
[78 85 78 88 85 72 90 65 80 85]

Array Information:
Dimensions: 1
Shape: (10,)
Size: 10

Unique values and their occurrences:
Value: 78  Count: 2
Value: 85  Count: 3
Value: 88  Count: 1
Value: 72  Count: 1
Value: 90  Count: 1
Value: 65  Count: 1
Value: 80  Count: 1

(Exact output depends on the values added and indices removed.)

================================================================================
KEY TAKEAWAYS
================================================================================

This project helped me understand how to:

  • Modify NumPy arrays by adding values with np.append()
  • Combine multiple arrays using np.concatenate()
  • Remove elements using specific indices with np.delete()
  • Inspect array structure using np.ndim(), .shape, and .size
  • Find unique values and their frequencies with np.unique()
  • Organize NumPy operations into reusable custom functions

================================================================================
FUTURE IMPROVEMENTS
================================================================================

Possible improvements include:

  • Add a menu-driven interface for user interaction
  • Allow users to enter values interactively
  • Add search functionality to find specific values
  • Add sorting functionality to the array
  • Calculate statistics such as mean, median, and standard deviation
  • Import data from CSV files
  • Export modified arrays to files
  • Support 2D arrays (matrices)
  • Add error handling for invalid indices
  • Build an interactive student-score management system

================================================================================
QUICK REFERENCE
================================================================================

+---------------------+--------------------------------------------------------+
| Function / Concept  | Description                                            |
+---------------------+--------------------------------------------------------+
| np.append(arr, vals)| Returns a new array with values appended               |
| np.concatenate((a,b))| Joins arrays along an existing axis                   |
| np.delete(arr, idx) | Returns a new array with elements removed             |
| np.ndim(arr)        | Returns the number of dimensions                       |
| arr.shape           | Returns a tuple with size of each dimension            |
| arr.size            | Returns the total number of elements                   |
| np.unique(arr, return_counts=True) | Returns unique values and their counts        |
| arr.copy()          | Creates a copy of the array                            |
+---------------------+--------------------------------------------------------+

================================================================================
STATUS
================================================================================

  Status       : ✅ Completed
  Section      : 10 — Array Manipulation
  Project      : Array Manager
  Language     : Python
  Library      : NumPy

================================================================================
End of Document
================================================================================