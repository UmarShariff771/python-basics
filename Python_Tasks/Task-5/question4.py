# 4. Write a lambda function to check if a given string is a number

# List of strings to test
test_strings = ["12345", "98a76", "007", "45.6", "hello", ""]

# Lambda function used with map to check if each string contains only digits
isString = map(lambda word: word.isdigit(), test_strings)

# Convert result to list and print
print(list(isString))