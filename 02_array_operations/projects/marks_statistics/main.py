import numpy as np

marks = np.array([45, 78, 92, 67, 88, 34, 95, 73, 81, 59])
pass_marks = marks[marks >= 50]

print("Total marks:", np.sum(marks))
print("Total passing marks:", np.sum(pass_marks))
print("Average marks:", np.mean(marks))
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))   
print("Range between highest and lowest marks:", np.ptp(marks))  # Peak to peak (max - min) 
print("Number of students who passed:", pass_marks.size)
print("Number of students who failed:", marks.size - pass_marks.size )
