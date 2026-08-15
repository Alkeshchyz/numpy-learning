# NumPy Array Basics — Notes

This section covers the fundamental concepts of creating, initializing, and inspecting NumPy arrays.

## 1. Importing NumPy

NumPy is commonly imported using the alias `np`.

```python
import numpy as np
```

## 2. Creating NumPy Arrays

### 1D Array

```python
a = np.array([1, 2, 3])
```

A 1D array has one dimension (Rank 1).

### 2D Array

```python
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

A 2D array has two dimensions (Rank 2).

## 3. Specifying Data Type

A data type can be specified when creating an array.

```python
np.array([1, 2, 3], dtype=bool)
```

Other data types can also be used, such as `float`.

## 4. Creating Arrays with `arange()`

`np.arange()` creates values within a specified range.

```python
np.arange(1, 11)
```

This creates values from 1 up to, but not including, 11.

## 5. Reshaping Arrays

`reshape()` changes the dimensions of an array.

```python
np.arange(1, 11).reshape(2, 5)
```

The values are reshaped into 2 rows and 5 columns.

## 6. Creating Arrays of Ones and Zeros

### Ones

```python
np.ones((3, 4))
```

Creates a 3 × 4 array filled with ones.

### Zeros

```python
np.zeros((3, 4))
```

Creates a 3 × 4 array filled with zeros.

## 7. Linear Spacing

`np.linspace()` creates a specified number of evenly spaced values between two limits.

```python
np.linspace(-10, 10, 8)
```

This creates 8 evenly spaced values between -10 and 10.

## 8. Identity Matrix

`np.identity()` creates a square matrix with ones on the main diagonal and zeros elsewhere.

```python
np.identity(3)
```

Creates a 3 × 3 identity matrix.

---

# Array Attributes

NumPy arrays provide several useful attributes for understanding their structure.

## `ndim`

Returns the number of dimensions.

```python
a.ndim
```

## `shape`

Returns the dimensions of the array.

```python
a.shape
```

For a 2D array, this represents the number of rows and columns.

## `size`

Returns the total number of elements.

```python
a.size
```

## `itemsize`

Returns the number of bytes used by each element.

```python
a.itemsize
```

## `dtype`

Returns the data type of the elements.

```python
a.dtype
```

## `astype()`

Converts an array to another data type.

```python
a.astype(np.int32)
```

---

# Key Takeaways

- NumPy arrays can be 1D, 2D, or have more dimensions.
- `np.array()` is used to create arrays.
- `arange()` creates values within a range.
- `reshape()` changes the structure of an array.
- `ones()`, `zeros()`, and `identity()` help initialize arrays.
- `linspace()` creates evenly spaced values.
- Array attributes such as `ndim`, `shape`, `size`, `itemsize`, and `dtype` help inspect an array.
- `astype()` can be used to convert an array's data type.

## Status

Section 01 — Array Basics ✅