import numpy as np

student_marks = np.array([45, 78, 92, 67, 88, 34, 95, 73, 81, 59])
print("Student Marks:", student_marks)  # [45 78 92 67 88 34 95 73 81 59]

number_of_students = student_marks.size
print("Number of Students:", number_of_students)  # 10

print("Dimensions of the array:", student_marks.ndim)  # 1
print("Shape of the array:", student_marks.shape)  # (10,)
print("Size of the array:", student_marks.size)  # 10
print("Item size (in bytes):", student_marks.itemsize)  # 8 (bytes per element)
print("Data type of the array:", student_marks.dtype)  # int64


Average_marks = np.mean(student_marks)
print("Average Marks:", Average_marks)  # 71.0

highest_marks = np.max(student_marks)
print("Highest Marks:", highest_marks)  # 95

lowest_marks = np.min(student_marks)
print("Lowest Marks:", lowest_marks)  # 34  

float_marks = student_marks.astype(np.float64)
print("Marks as float:", float_marks)  # [45. 78. 92. 67. 88. 34. 95. 73. 81. 59.]
    