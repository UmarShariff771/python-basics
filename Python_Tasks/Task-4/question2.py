# 2. Given a python list [10, 501, 22, 37, 100, 999, 87, 351]
# your task is to count all the Prime Numbers and create a new python list which will contain all the prime numbers in it

numberList = [10, 501, 22, 37, 100, 999, 87, 351]
primeNumberList = []

# Iterating the number list in a for loop
for number in numberList:
    # Declared a counter as zero
    # For each number iterating in the list starts with counter as 0
    counter = 0
    # Iterating again starting with 2 till the iterated number as range
    for i in range (2, number):
        # If the number is divisible add counter and break the loop
        if (number % i == 0):
            counter += 1
            break
    # If the counter is zero then its prime number
    # since 1 and the number itself was not counted since max length is the number
    if (counter == 0):
        primeNumberList.append(number)

print(primeNumberList)