import numpy as np

marks = np.array([45, 67, 89, 32, 76, 91, 54, 38, 82, 95])
# Average marks
# Highest mark
# Lowest mark
# Total marks
# Which students scored 50 or above
# How many students scored 50 or above
# The range between the highest and lowest marks
print("Average marks:", np.mean(marks))
print("Highest mark:", np.max(marks))
print("Lowest mark:", np.min(marks))
print("Total marks:", np.sum(marks))
print("Students who scored 50 or above:", marks[marks >= 50])
print("Number of students who scored 50 or above:", np.sum(marks >= 50))
print("Range between highest and lowest marks:", np.ptp(marks))  # Peak to peak (max - min)