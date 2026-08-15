import numpy as np

# Daily sales for 10 days
sales = np.array([
    120, 150, 180, 100, 200,
    220, 170, 250, 300, 280
])

# TODO:
# 1. Calculate cumulative sales.
# 2. Find the total sales.
# 3. Find the highest daily sale.
# 4. Find the lowest daily sale.
# 5. Calculate the average daily sale.
#
# Useful NumPy functions:
# np.cumsum()
# np.sum()
# np.max()
# np.min()
# np.mean()

cumulative_sales = np.cumsum(sales)
total_sales = np.sum(sales)
highest_sale = np.max(sales)
lowest_sale = np.min(sales)
average_sale = np.mean(sales)

print("Cumulative sales:")
print(cumulative_sales)
print("Total sales:", total_sales)
print("Highest daily sale:", highest_sale)
print("Lowest daily sale:", lowest_sale)
print("Average daily sale:", average_sale)