import numpy as np

marks = np.array([45, 78, 92, 67, 88, 34, 95, 73, 81, 59])

# 1. Marks at indexes 0, 3, 6 (Fancy Indexing)
print("Marks at indexes 0, 3, 6:", marks[[0, 3, 6]])

# 2. Marks at indexes 1, 4, 8 (Fancy Indexing)
print("Marks at indexes 1, 4, 8:", marks[[1, 4, 8]])

# 3. Marks greater than 75 (Boolean Indexing)
print("Marks > 75:", marks[marks > 75])

# 4. Marks less than 60 (Boolean Indexing)
print("Marks < 60:", marks[marks < 60])

# 5. All even marks
print("Even marks:", marks[marks % 2 == 0])

# 6. Marks greater than 70 and less than 90 (Compound Boolean Filter)
print("Marks > 70 and < 90:", marks[(marks > 70) & (marks < 90)])