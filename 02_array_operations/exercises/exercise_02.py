import numpy as np

prices = np.array([100, 200, 300, 400, 500])
discount = np.array([10, 20, 30, 40, 50])

final_prices = prices - discount

print("Price after discount:", final_prices)
print("Original prices:", prices)
print("Total original price:", np.sum(prices))
print("Total cost after discount:", np.sum(final_prices))
print("Total discount:", np.sum(discount))
print("Average final price:", np.mean(final_prices))