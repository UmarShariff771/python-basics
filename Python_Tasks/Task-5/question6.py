# 6. Create a lambda function to generate a fibonacci series up to n terms.

# Get number of terms from user
number = int(input("Enter your number for fibonacci...."))

# Lambda function to add two numbers
fib = lambda a, b: a + b

# Initialize first two fibonacci numbers
a = 0
b = 1

# If user wants only one term
if number == 1:
    print(a)

# If user wants two terms
elif number == 2:
    print(a)
    print(b)

# If user wants more than two terms
else:
    # Print first two numbers
    print(a)
    print(b)
    # Generate remaining fibonacci numbers using loop
    for i in range(number - 2):
        c = fib(a, b)
        print(c)
        a = b
        b = c