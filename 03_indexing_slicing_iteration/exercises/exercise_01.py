import numpy as np

numbers = np.array([15, 25, 35, 45, 55, 65, 75, 85])

print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])
print("Second-last element:", numbers[-2])
print("Elements from 35 to 65:", numbers[2:6])
print("Every second element:", numbers[::2])