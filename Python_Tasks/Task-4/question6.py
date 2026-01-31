# 6. You have been given three lists. Your task is to find the duplicates in the three lists.
# Write a program for same. You can use your own python lists.
from multiprocessing.reduction import duplicate

# The three lists
list1 = [3, 7, 12, 19, 25, 30, 42, 56]
list2 = [5, 7, 14, 19, 22, 30, 41, 60]
list3 = [1, 7, 9, 12, 19, 28, 30, 50]

# Combining the three list into a single list
combinedList = list1 + list2 + list3
# Declare a unique list to iterate the unique values
uniqueList = []
# Declare to iterate the duplicate items
duplicateList = []
# Declare to iterate the non-duplicate items
nonDuplicateList = []

# Iterate the combined list one by one
for item1 in combinedList:
    # Counting the number of times the item got repeated
    count = 0
    # If item present in the unique list then continue the loop with next iteration
    if item1 in uniqueList:
        continue
    # Iterate the items to check with one another
    for item2 in combinedList:
        # if the both iterations match then count as one
        if item1 == item2:
            count += 1
    # If count is 1 then it's unique without duplicate
    if count == 1:
        print(str(item1) + " is an unique item" )
        nonDuplicateList.append(item1)
    # else it contains duplicates
    else:
        print(str(item1) + " is a duplicate item")
        duplicateList.append(item1)
    # Push the iterated item to uniques list so that it need not repeat again for iteration
    uniqueList.append(item1)

print("The duplicate list is....")
print(duplicateList)
print("The non-duplicate list is....")
print(nonDuplicateList)