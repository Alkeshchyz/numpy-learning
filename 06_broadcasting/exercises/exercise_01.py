import numpy as np

# Original dataset
prices = np.array([100, 200, 300, 400, 500])
print("Original prices:")
print(prices)

# 1. Add 50 to every price
print("\nAdd 50:")
print(prices + 50)

# 2. Subtract 20 from every price
print("\nSubtract 20:")
print(prices - 20)

# 3. Multiply every price by 2
print("\nMultiply by 2:")
print(prices * 2)

# 4. Divide every price by 10
print("\nDivide by 10:")
print(prices / 10)

# 5. Calculate a 10% discount on every price
discounted = prices * 0.90
print("\n10% Discounted prices:")
print(discounted)