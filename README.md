# NumPy Learning

A structured, hands-on repository for learning **NumPy** - the fundamental Python library for fast numerical computing. It is designed to move from array basics to practical data manipulation, linear algebra, and small projects through concise examples and exercises.

## What You Will Learn

- Create, inspect, and reshape NumPy arrays
- Select and update values with indexing, slicing, and boolean masks
- Perform fast element-wise calculations with vectorization and broadcasting
- Use aggregation, sorting, and random-number utilities
- Work with matrices and basic linear algebra
- Apply NumPy concepts in practical mini-projects

## Why NumPy?

NumPy provides the `ndarray`: a compact, efficient multidimensional array. It makes numerical operations clearer and usually much faster than writing equivalent loops with standard Python lists. NumPy is also a foundation for libraries such as pandas, SciPy, scikit-learn, and many data-science tools.

## Learning Path

Work through the topics in order. Each section should include short notes, runnable examples, and exercises.

| Module | Topic | Key skills |
| --- | --- | --- |
| 01 | Introduction to NumPy | Installation, importing NumPy, `ndarray` basics |
| 02 | Creating Arrays | Lists, ranges, zeros, ones, identity matrices, random arrays |
| 03 | Array Attributes | Shape, dimensions, size, data type |
| 04 | Indexing and Slicing | Selecting rows, columns, ranges, and individual values |
| 05 | Array Operations | Arithmetic, comparisons, universal functions |
| 06 | Broadcasting | Combining arrays with compatible shapes |
| 07 | Reshaping and Combining | `reshape`, `flatten`, stacking, splitting, transposing |
| 08 | Aggregation and Statistics | Sum, mean, min, max, standard deviation, axis operations |
| 09 | Boolean Masking | Filtering and conditional updates |
| 10 | Random Numbers | Sampling, seeds, permutations, reproducible experiments |
| 11 | Linear Algebra | Dot products, matrix multiplication, solving systems |
| 12 | Practice Projects | Applying concepts to small data problems |

## Suggested Repository Structure

```text
numpy-learning/
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 01_introduction.ipynb
│   ├── 02_array_creation.ipynb
│   └── ...
├── exercises/
│   ├── 01_basics.py
│   ├── 02_indexing.py
│   └── solutions/
├── projects/
│   ├── image_array_basics/
│   └── grade_analysis/
└── data/
    └── sample_data.csv
```

## Getting Started

### Prerequisites

- Python 3.9 or newer
- A terminal, code editor, or Jupyter Notebook environment

### Install NumPy

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Install the dependency:

```bash
pip install numpy
```

For notebook-based lessons, also install Jupyter:

```bash
pip install jupyter
jupyter notebook
```

## Quick Start

```python
import numpy as np

# Create a 2 x 3 array
scores = np.array([[82, 91, 76], [88, 79, 95]])

print(scores.shape)        # (2, 3)
print(scores.mean())       # 85.166...
print(scores + 5)          # Adds 5 to every value
print(scores[:, 1])        # Selects the second column
```

## Core Concepts at a Glance

### Create arrays

```python
import numpy as np

zeros = np.zeros((2, 3))
sequence = np.arange(0, 10, 2)
grid = np.linspace(0, 1, 5)
identity = np.eye(3)
```

### Index and filter data

```python
values = np.array([10, 25, 30, 45, 50])

print(values[1:4])          # [25 30 45]
print(values[values >= 30]) # [30 45 50]
```

### Use vectorized operations

```python
prices = np.array([12.5, 8.0, 15.0])
discounted_prices = prices * 0.9
```

Avoid explicit loops when an array operation expresses the same idea more directly.

### Understand broadcasting

```python
sales = np.array([[100, 120, 90], [80, 110, 95]])
bonus = np.array([10, 10, 10])

adjusted_sales = sales + bonus
```

Here, the one-dimensional `bonus` array is applied to each row of `sales`.

## Practice Ideas

- Build a multiplication table with a two-dimensional array.
- Normalize a set of test scores to the 0–1 range.
- Find the highest-scoring student in each subject.
- Simulate coin tosses or dice rolls and summarize the outcomes.
- Convert a grayscale image represented as an array into a threshold mask.
- Implement simple matrix operations without Python loops.

## How to Study

1. Read one lesson and run every example yourself.
2. Change the inputs and predict the result before executing the code.
3. Complete the matching exercise without looking at a solution.
4. Write down unfamiliar functions in your own words.
5. Revisit earlier topics while building projects.

## Useful References

- [NumPy documentation](https://numpy.org/doc/)
- [NumPy quickstart tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy API reference](https://numpy.org/doc/stable/reference/)

## Contributing

Contributions are welcome. Useful additions include:

- Clear lesson notebooks and examples
- New exercises with solutions
- Corrections or improved explanations
- Small, well-documented projects

Please keep examples focused, runnable, and accompanied by a short explanation of the concept they demonstrate.

## License

This project is intended for educational use. Add a license file (for example, MIT) if you plan to distribute or accept contributions to the repository.

---

Happy learning - experiment often, inspect array shapes carefully, and let NumPy do the looping for you.
