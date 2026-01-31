# 7. Write a python program to find the first non-repeating elements in a given list of integers

numbers = [4, 5, 1, 2, 0, 4, 5, 2, 3, 1, 6, 3]
# Declare a unique list to iterate the unique values
uniqueList = []
# Declare to iterate the non-repeating items
nonRepeat = []

# Iterate the combined list one by one
for number1 in numbers:
    # Counting the number of times the item got repeated
    count = 0
    # If item present in the unique list then continue the loop with next iteration
    if number1 in uniqueList:
        continue
    # Iterate the items to check with one another
    for number2 in numbers:
        # if the both iterations match then count as one
        if number1 == number2:
            count += 1
    # If count is 1 then it's unique and non-repeating
    if count == 1:
        nonRepeat.append(number1)

    uniqueList.append(number1)

print("The first non repeating element element is " + str(nonRepeat[0]))