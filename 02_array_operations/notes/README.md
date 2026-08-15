# Section 02 — Array Operations README Files

This document contains the Markdown contents for the three Section 02 README files.

================================================================================
FILE: 02_array_operations/notes/README.md
================================================================================

# NumPy Array Operations

This section covers basic operations performed on NumPy arrays, including arithmetic, relational, aggregation, statistical, and mathematical operations.

---

## 1. Arithmetic Operations

NumPy supports element-wise arithmetic operations between arrays.

```python
import numpy as np

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

### Common Arithmetic Operators

| Operation | Operator |
|---|---|
| Addition | `+` |
| Subtraction | `-` |
| Multiplication | `*` |
| Division | `/` |
| Floor Division | `//` |
| Modulus | `%` |
| Exponentiation | `**` |

Example:

```python
a // b
a % b
a ** b
```

Operations are performed element by element.

---

## 2. Mathematical Functions

NumPy provides built-in mathematical functions for array calculations.

### Square Root

```python
np.sqrt(a)
```

### Power

```python
np.power(a, 2)
```

### Sine

```python
np.sin(a)
```

### Cosine

```python
np.cos(a)
```

### Logarithm

```python
np.log(a)
```

### Exponential

```python
np.exp(a)
```

---

## 3. Relational Operations

Relational operators compare each element of an array and return Boolean values.

```python
a = np.array([10, 20, 30, 40, 50])

print(a > 25)
print(a < 30)
print(a >= 30)
print(a <= 30)
print(a == 30)
print(a != 30)
```

Example output:

```text
[False False  True  True  True]
```

The result is a Boolean array containing `True` and `False`.

---

## 4. Aggregation Functions

Aggregation functions are used to summarize values in an array.

### Sum

```python
np.sum(a)
```

### Product

```python
np.prod(a)
```

### Minimum

```python
np.min(a)
```

### Maximum

```python
np.max(a)
```

---

## 5. Working with Axis

For multidimensional arrays, the `axis` parameter determines the direction of the operation.

```python
b = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

### `axis=0`

Performs the operation column-wise.

```python
np.sum(b, axis=0)
```

### `axis=1`

Performs the operation row-wise.

```python
np.sum(b, axis=1)
```

### Quick Reference

```text
axis=0 → column-wise
axis=1 → row-wise
```

---

## 6. Statistical Functions

NumPy provides several functions for statistical analysis.

### Mean

```python
np.mean(a)
```

Calculates the average value.

### Median

```python
np.median(a)
```

Calculates the median value.

### Standard Deviation

```python
np.std(a)
```

Calculates the standard deviation.

### Variance

```python
np.var(a)
```

Calculates the variance.

### Range

```python
np.ptp(a)
```

Returns the difference between the maximum and minimum values.

```text
Range = Maximum - Minimum
```

---

## 7. Summary

| Category | NumPy Functions / Operators |
|---|---|
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| Mathematical | `sqrt()`, `power()`, `sin()`, `cos()`, `log()`, `exp()` |
| Relational | `>`, `<`, `>=`, `<=`, `==`, `!=` |
| Aggregation | `sum()`, `prod()`, `min()`, `max()` |
| Statistics | `mean()`, `median()`, `std()`, `var()`, `ptp()` |
| Axis | `axis=0`, `axis=1` |

---

## Learning Outcome

After completing this section, I can:

- Perform arithmetic operations on NumPy arrays.
- Compare array elements using relational operators.
- Calculate sums, products, minimums, and maximums.
- Understand the use of `axis` in 2D arrays.
- Perform basic statistical calculations.
- Apply NumPy mathematical functions.

---

**Status:** Completed ✅

================================================================================
FILE: 02_array_operations/exercises/README.md
================================================================================

# Section 02 — Exercises

This folder contains exercises for practicing NumPy array operations.

---

## Exercise 01 — Student Marks

### Objective

Practice basic aggregation and statistical operations using a NumPy array.

### Concepts Practiced

- `np.sum()`
- `np.mean()`
- `np.max()`
- `np.min()`
- `np.ptp()`
- Relational operators
- Boolean arrays

### File

```text
exercise_01.py
```

---

## Exercise 02 — Price and Discount

### Objective

Practice performing arithmetic operations between two NumPy arrays.

### Concepts Practiced

- Array-to-array operations
- Subtraction
- `np.sum()`
- `np.mean()`

### File

```text
exercise_02.py
```

---

## Exercise 03 — Student Performance Analysis

### Objective

Combine multiple NumPy operations to analyze student performance.

### Concepts Practiced

- Arithmetic operations
- Relational operations
- Aggregation
- Statistical functions
- Boolean conditions

### File

```text
exercise_03.py
```

---

## Learning Goal

These exercises are designed to strengthen the understanding of NumPy array operations through practical coding.

The focus is on writing simple NumPy code and performing operations directly on arrays instead of relying on unnecessary loops.

---

## Completion Status

| Exercise | Status |
|---|---|
| Exercise 01 | ✅ Completed |
| Exercise 02 | ✅ Completed |
| Exercise 03 | ✅ Completed |

**Section 02 Exercises: Completed ✅**

================================================================================
FILE: 02_array_operations/projects/marks_statistics/README.md
================================================================================

# Marks Statistics Analyzer

A beginner-friendly NumPy project that analyzes student marks using array operations and statistical functions.

---

## Objective

The objective of this project is to apply the NumPy concepts learned in **Section 02 — Array Operations** to a simple real-world-style problem.

The program takes a set of student marks and generates basic statistical information.

---

## Dataset

The project uses the following marks:

```python
import numpy as np

marks = np.array([45, 78, 92, 67, 88, 34, 95, 73, 81, 59])
```

---

## Features

The program calculates:

- Total marks
- Average marks
- Highest mark
- Lowest mark
- Range of marks
- Number of subjects passed
- Number of subjects failed

---

## NumPy Concepts Used

### Array Creation

```python
np.array()
```

### Aggregation

```python
np.sum()
np.max()
np.min()
```

### Statistics

```python
np.mean()
np.ptp()
```

### Relational Operations

The project uses Boolean conditions to determine whether a mark meets the passing requirement.

---

## Project Structure

```text
marks_statistics/
├── main.py
└── README.md
```

---

## Example Output

```text
Total Marks: ...
Average Marks: ...
Highest Mark: ...
Lowest Mark: ...
Range: ...
Subjects Passed: ...
Subjects Failed: ...
```

---

## Learning Outcome

Through this project, I practiced combining multiple NumPy operations to perform a basic analysis of numerical data.

This project helped me understand how NumPy can be used to process and analyze data efficiently.

---

## Status

**Completed ✅**
