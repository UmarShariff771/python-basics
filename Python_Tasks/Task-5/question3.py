# 3. Write a list comprehension that creates a new list of squares of even numbers
# from a given list, using a lambda function to check for even numbers

# Given list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Normal lambda steps
# even = list(filter(lambda num: num % 2 == 0, numbers))
# square = list(map(lambda num : num * num, even))

# List comprehension to get squares of even numbers
# Lambda is used to check if a number is even
square = [n * n for n in numbers if(lambda num: num % 2 == 0)(n)]

# Print the result
print(square)