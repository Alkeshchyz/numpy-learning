import numpy as np

marks = np.array([45, 78, 92, 67, 88, 34, 95, 73, 81, 59])

# 1. Indexes of marks greater than 80
print("Indexes of marks > 80:", np.where(marks > 80)[0])

# 2. Indexes of marks below 50
print("Indexes of marks < 50:", np.where(marks < 50)[0])

# 3. Replace marks below 50 with 0
print("Replaced < 50 with 0:", np.where(marks < 50, 0, marks))

# 4. Replace marks greater than or equal to 90 with 100
print("Replaced >= 90 with 100:", np.where(marks >= 90, 100, marks))

# 5. Classify marks into "Pass" or "Fail"
status = np.where(marks >= 60, "Pass", "Fail")
print("Pass/Fail Status:", status)