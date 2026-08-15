PREDICTION ERROR ANALYZER Custom Functions & Error Analysis (Section 07)
================================================================================

OVERVIEW
--------
Prediction Error Analyzer is a practical NumPy project that analyzes the
difference between actual and predicted values using custom Python functions
and NumPy mathematical operations. The program demonstrates how to measure
prediction accuracy using various error metrics.

================================================================================
PROJECT OBJECTIVE
================================================================================

The purpose of this project is to combine the concepts learned in Section 07 —
Custom Functions into a practical numerical analysis program.

The project calculates:
  • Prediction errors
  • Absolute errors
  • Mean Absolute Error (MAE)
  • Mean Squared Error (MSE)
  • Sigmoid-transformed errors

It demonstrates how custom functions can be combined with NumPy arrays to
perform mathematical analysis efficiently.

================================================================================
DATASET
================================================================================

The project uses two NumPy arrays:

    import numpy as np

    actual = np.array([10, 20, 30, 40, 50])
    predicted = np.array([12, 18, 29, 43, 48])

Actual values:
    [10 20 30 40 50]

Predicted values:
    [12 18 29 43 48]

================================================================================
ERROR ANALYSIS CALCULATIONS
================================================================================

1. Prediction Errors
--------------------
The prediction error is calculated using:

    errors = actual - predicted

Result:
    [-2  2  1 -3  2]

Interpretation:
  • Negative value → Prediction was higher than actual value
  • Positive value → Prediction was lower than actual value

2. Squared Errors
-----------------
Squared errors are calculated to penalize larger errors more heavily:

    squared_error = errors ** 2

For the project data:

    Errors:      [-2,  2,  1, -3,  2]
    Squared:     [ 4,  4,  1,  9,  4]

3. Mean Squared Error (MSE)
---------------------------
The project defines a custom function:

    def mean_squared_error(actual, predicted):
        error = actual - predicted
        squared_error = error ** 2
        return np.mean(squared_error)

Formula:
    MSE = mean((actual - predicted)²)

Calculation:
    MSE = (4 + 4 + 1 + 9 + 4) / 5
        = 22 / 5
        = 4.4

Mean Squared Error = 4.4

A lower MSE generally indicates that predictions are closer to the actual
values.

4. Absolute Errors
------------------
The project calculates absolute errors using:

    absolute_errors = np.abs(errors)

Result:
    [2 2 1 3 2]

The np.abs() function removes the negative sign and gives the magnitude of
each prediction error.

5. Mean Absolute Error (MAE)
----------------------------
The Mean Absolute Error is calculated using:

    mean_absolute_error = np.mean(absolute_errors)

Calculation:
    MAE = (2 + 2 + 1 + 3 + 2) / 5
        = 10 / 5
        = 2.0

Mean Absolute Error = 2.0

MAE represents the average absolute difference between the actual and
predicted values.

6. Sigmoid Function
-------------------
The project also defines a custom sigmoid function:

    def sigmoid(array):
        return 1 / (1 + np.exp(-array))

The sigmoid formula is:
    Sigmoid(x) = 1 / (1 + e^(-x))

The function is applied to the prediction errors:

    sigmoid_errors = sigmoid(errors)

This transforms the errors into values between 0 and 1.

For example:
    Sigmoid(-2) = 1 / (1 + e^(2)) ≈ 0.119
    Sigmoid(2)  = 1 / (1 + e^(-2)) ≈ 0.881

================================================================================
CONCEPTS DEMONSTRATED
================================================================================

+---------------------------+--------------------------------------------------+
| Concept                   | Usage                                            |
+---------------------------+--------------------------------------------------+
| NumPy arrays              | Store actual and predicted values                |
| Custom functions          | Create reusable calculations                     |
| Function parameters       | Pass arrays into functions                       |
| return                    | Return calculated results                        |
| Array subtraction         | Calculate prediction errors                      |
| np.abs()                  | Calculate absolute errors                        |
| np.mean()                 | Calculate averages                               |
| np.exp()                  | Calculate exponential values                     |
| Squaring arrays           | Calculate squared errors                         |
| Sigmoid                   | Transform numerical values                       |
+---------------------------+--------------------------------------------------+

================================================================================
PROJECT STRUCTURE
================================================================================

    prediction_error_analyzer/
    ├── main.py
    └── README.md

  main.py    – Contains the complete Prediction Error Analyzer program.
  README.md  – Contains documentation explaining the project, calculations,
               concepts, and results.

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

Actual values:
[10 20 30 40 50]

Predicted values:
[12 18 29 43 48]

Prediction Errors:
[-2  2  1 -3  2]

Squared Errors:
[4 4 1 9 4]

Mean Squared Error (MSE):
4.4

Absolute Errors:
[2 2 1 3 2]

Mean Absolute Error (MAE):
2.0

Sigmoid of Prediction Errors:
[0.11920292 0.88079708 0.73105858 0.04742587 0.88079708]

================================================================================
KEY TAKEAWAYS
================================================================================

This project helped me understand how to:

  • Create reusable custom functions
  • Pass NumPy arrays into functions
  • Return calculated results
  • Perform element-wise mathematical operations
  • Measure prediction accuracy
  • Calculate MSE and MAE
  • Use NumPy mathematical functions (np.abs, np.mean, np.exp)
  • Apply custom mathematical transformations to arrays

================================================================================
COMPARISON OF ERROR METRICS
================================================================================

+---------------------------+----------------------------------------------+
| Metric                    | Characteristics                              |
+---------------------------+----------------------------------------------+
| Prediction Errors         | Raw differences (can be positive/negative)   |
| Absolute Errors           | Magnitude of errors (always positive)        |
| Mean Absolute Error (MAE) | Average magnitude of errors                  |
| Mean Squared Error (MSE)  | Penalizes large errors more heavily          |
| Sigmoid Errors            | Transforms errors to 0-1 range               |
+---------------------------+----------------------------------------------+

================================================================================
FUTURE IMPROVEMENTS
================================================================================

Possible improvements include:

  • Accepting user input for actual and predicted values
  • Calculating additional metrics such as RMSE (Root Mean Squared Error)
  • Adding prediction accuracy categories
  • Comparing multiple prediction models
  • Creating visualizations of prediction errors
  • Reading prediction data from CSV files
  • Adding R² score calculation

================================================================================
QUICK REFERENCE
================================================================================

+---------------------------+----------------------------------------------+
| Function / Concept        | Description                                  |
+---------------------------+----------------------------------------------+
| actual - predicted        | Calculate prediction errors                  |
| errors ** 2               | Square each error (MSE calculation)          |
| np.abs(errors)            | Get absolute value of each error             |
| np.mean(array)            | Calculate the mean of an array               |
| np.exp(array)             | Calculate exponential of each element        |
| sigmoid(x) = 1/(1+e^(-x)) | Sigmoid function (output in 0-1 range)       |
| MSE                       | Mean Squared Error                           |
| MAE                       | Mean Absolute Error                          |
+---------------------------+----------------------------------------------+

================================================================================
STATUS
================================================================================

  Status       : ✅ Completed
  Section      : 07 — Custom Functions
  Project      : Prediction Error Analyzer
  Library      : NumPy
  Language     : Python

================================================================================
End of Document
================================================================================