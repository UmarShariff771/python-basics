# 10. Given the list [4, 2, -3, 1, 6]
# Write a python program to find if there is a sub-list with sum equal to zero

nums = [4, 2, -3, 1, 6]

# Declaring a boolean found as false initially
found = False

# Iterating the list length
for i in range(len(nums)):
    # addition of iterating number is declared as zero
    total = 0
    # adding the number starting from the next number
    for j in range(i, len(nums)):
        # adding the numbers to the total
        total = total + nums[j]
        print(total)
        # If total becomes zero break the j iteration
        if total == 0:
            found = True
            break
    # If the found in true break the i iteration
    if found:
        break
# checking the condition
if found:
    print("Sub list with sum exists")
else:
    print("Not found")