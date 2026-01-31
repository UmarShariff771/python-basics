# 1. You have been given a python list [10, 501, 22, 37, 100, 999, 87, 351]
# Your task is to create two list one which have all the Even Numbers and Another List with odd numbers

numberList = [10, 501, 22, 37, 100, 999, 87, 351]

# Create an odd and even blank list to iterate
extractEven = []
extractOdd = []

# Iterate using for loop
for number in numberList:
    # Store the iterating value one by one
    num = number
    # Check number divisible by 2
    if(number % 2 == 0):
        extractEven.append(num)
        extractEven.sort()
    else:
        extractOdd.append(num)
        extractOdd.sort()

# Print the extracted list
print(extractEven)
print(extractOdd)