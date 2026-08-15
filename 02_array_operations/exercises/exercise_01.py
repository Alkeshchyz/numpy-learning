import numpy as np

marks = np.array([55, 72, 91, 43, 86, 67, 78, 95, 61, 38])

print("Total marks:", np.sum(marks))
print("Average marks:", np.mean(marks))
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Range between highest and lowest marks:",np.ptp(marks))  # Peak to peak (max - min)
print("Each marks is greater than or equal to 50:", marks >= 50)