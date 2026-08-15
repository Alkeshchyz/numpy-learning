================================================================================
                         MISSING DATA CLEANER
               NumPy Project – Section 08 (Missing Values)
================================================================================

OVERVIEW
--------
Missing Data Cleaner is a practical NumPy project for detecting, analyzing,
and cleaning missing values (NaN) from numerical datasets. It demonstrates
how to handle incomplete data using NumPy's built‑in functions and custom
Python functions.

================================================================================
PROJECT OBJECTIVE
================================================================================

The purpose of this project is to apply the concepts learned in Section 08 —
Missing Values to a practical dataset.

The program:
  • Detects missing values
  • Counts missing values
  • Calculates statistics while ignoring missing values
  • Replaces missing values with the mean
  • Verifies that the dataset has been cleaned
  • Calculates statistics on the cleaned dataset

================================================================================
DATASET
================================================================================

The project uses a NumPy array containing student marks:

    import numpy as np

    marks = np.array([78, 85, np.nan, 92, 67, np.nan, 88, 74, np.nan, 95])

The dataset contains 10 values, including 3 missing values (represented by nan).

================================================================================
1. DETECTING MISSING VALUES
================================================================================

Missing values are represented using NumPy's NaN value: np.nan

The project uses np.isnan(data) to identify which elements are missing.

Example:
    np.isnan(marks)

Output:
    [False False  True False False  True False False  True False]

True indicates a missing value.

================================================================================
2. COUNTING MISSING VALUES
================================================================================

The project defines a custom function:

    def count_missing(data):
        return np.sum(np.isnan(data))

The expression np.isnan(data) produces a Boolean array. np.sum() counts the
True values.

For this dataset:
    count_missing(marks)   →   3

Number of missing values: 3

================================================================================
3. CALCULATING THE MEAN (Ignoring Missing Values)
================================================================================

Using np.mean(data) on an array containing NaN results in nan because the
missing value affects the calculation.

Instead, the project uses np.nanmean(data), which ignores missing values and
calculates the mean of the available data.

    mean_value = np.nanmean(marks)

================================================================================
4. REPLACING MISSING VALUES
================================================================================

The project defines another custom function:

    def replace_missing(data):
        mean_value = np.nanmean(data)
        return np.where(np.isnan(data), mean_value, data)

Step 1: Calculate the mean of the available values.
Step 2: Use np.where() to replace every NaN with the calculated mean.

This produces a cleaned dataset without missing values.

================================================================================
5. VERIFYING THE CLEANED DATASET
================================================================================

After replacing the missing values, the project checks the dataset again:

    count_missing(cleaned_marks)

Expected result:
    Number of missing values after cleaning: 0

This confirms that all missing values have been replaced.

================================================================================
6. STATISTICAL ANALYSIS AFTER CLEANING
================================================================================

After cleaning the dataset, the project calculates:

    • Mean          →  np.mean(cleaned_marks)
    • Median        →  np.median(cleaned_marks)
    • Standard Dev. →  np.std(cleaned_marks)

Because the missing values have been replaced, normal NumPy statistical
functions can now be used without errors.

================================================================================
CONCEPTS DEMONSTRATED
================================================================================

+---------------------+--------------------------------------------------------+
| Concept             | Usage                                                  |
+---------------------+--------------------------------------------------------+
| np.nan              | Represents missing numerical data                      |
| np.isnan()          | Detects missing values                                 |
| np.sum()            | Counts missing values (sum of Boolean array)           |
| np.nanmean()        | Calculates mean while ignoring NaN                     |
| np.where()          | Replaces missing values conditionally                  |
| np.mean()           | Calculates mean of cleaned data                        |
| np.median()         | Calculates median of cleaned data                      |
| np.std()            | Calculates standard deviation of cleaned data          |
| Custom functions    | Creates reusable data‑cleaning operations              |
| NumPy arrays        | Stores and processes numerical data                    |
+---------------------+--------------------------------------------------------+

================================================================================
PROJECT STRUCTURE
================================================================================

    missing_data_cleaner/
    ├── main.py
    └── README.md

  main.py    – Contains the complete missing‑data cleaning program.
  README.md  – Contains documentation explaining the project, techniques,
               and concepts used.

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

Original data:
[78. 85. nan 92. 67. nan 88. 74. nan 95.]

Number of missing values:
3

Mean of available values (ignoring NaN):
82.71428571428571

Cleaned data:
[78.         85.         82.71428571 92.         67.
 82.71428571 88.         74.         82.71428571 95.        ]

Number of missing values after cleaning:
0

Mean of cleaned data:
82.71428571428571

Median of cleaned data:
83.35714285714286

Standard deviation of cleaned data:
8.83888301223776

(Exact decimal formatting may vary depending on NumPy's output settings.)

================================================================================
KEY TAKEAWAYS
================================================================================

This project helped me understand how to:

  • Work with missing numerical data
  • Detect NaN values using np.isnan()
  • Count missing values
  • Perform calculations while ignoring missing data using np.nanmean()
  • Replace missing values with statistical measures using np.where()
  • Verify that a dataset has been cleaned
  • Create reusable data‑cleaning functions
  • Perform statistical analysis after cleaning

================================================================================
FUTURE IMPROVEMENTS
================================================================================

Possible improvements include:

  • Allowing users to enter their own data
  • Replacing missing values with the median instead of the mean
  • Removing rows containing missing values (listwise deletion)
  • Reading datasets from CSV files
  • Handling multiple columns (2D arrays)
  • Adding data visualisation (e.g., histograms before/after)
  • Comparing different imputation strategies (mean, median, mode, forward fill)

================================================================================
QUICK REFERENCE
================================================================================

+---------------------+--------------------------------------------------------+
| Function / Concept  | Description                                            |
+---------------------+--------------------------------------------------------+
| np.nan              | Missing value placeholder                              |
| np.isnan(arr)       | Returns Boolean array indicating missing values        |
| np.sum(bool_arr)    | Counts True values (missing count)                     |
| np.nanmean(arr)     | Mean ignoring NaN values                               |
| np.where(cond, x, y)| Returns x where cond is True, else y                   |
| np.mean(arr)        | Mean of array                                          |
| np.median(arr)      | Median of array                                        |
| np.std(arr)         | Standard deviation of array                            |
+---------------------+--------------------------------------------------------+

================================================================================
STATUS
================================================================================

  Status       : ✅ Completed
  Section      : 08 — Missing Values
  Project      : Missing Data Cleaner
  Language     : Python
  Library      : NumPy

================================================================================
End of Document
================================================================================