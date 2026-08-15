import numpy as np

a = np.arange(1,11) # Create a NumPy 1D array with values from 1 to 10  
print(a)  # Output: [1 2 3 4 5 6 7 8 9 10]


b = np.ones((3, 4)) # Create a NumPy 2D array of shape (3, 4) filled with ones
print(b)  # Output: [[1. 1. 1. 1.]
        #          [1. 1. 1. 1.]
        #          [1. 1. 1. 1.]]

c = np.zeros((2, 3)) # Create a NumPy 2D array of shape (2, 3) filled with zeros
print(c)  # Output: [[0. 0. 0.]
        #          [0. 0. 0.]]  

d = np.linspace(-10, 10, 8) # Create a NumPy 1D array with 8 evenly spaced values from -10 to 10
print(d)  # Output: [-10.          -7.14285714  -4.28571429  -1.42857143   1.42857143   4.28571429   7.14285714  10.        ]

e = np.identity(3) # Create a 3x3 identity matrix
print(e)  # Output: [[1. 0. 0.] 
        #          [0. 1. 0.]
        #          [0. 0. 1.]]