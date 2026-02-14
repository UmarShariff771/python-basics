# 2. Given a list of numbers, use the reduce function and a lambda expression
# to calculate the product of all the numbers in the list.

# Import reduce function from functools module
from functools import reduce

# List of numbers
numbers = [2, 4, 3, 5, 2]

# Use reduce with lambda to multiply all numbers in the list
total = reduce(lambda a,b: a * b, numbers)

# Print the final product
print(total)
