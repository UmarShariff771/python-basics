# 9. You have been given a python list [10, 20, 30, 9] and value of 59.
# Write a python to find the triplet in the list whose sum is equal to the given value?

# Combinations
nums = [10, 20, 30, 9]

# Target value
target = 59

# Store values seperately
a = nums[0]
b = nums[1]
c = nums[2]
d = nums[3]

# Use if statement to do combinations of addition to get the target
if a + b + c == target:
    print("Triplet found:", a, b, c)
elif a + b + d == target:
    print("Triplet found:", a, b, d)
elif a + c + d == target:
    print("Triplet found:", a, c, d)
elif b + c + d == target:
    print("Triplet found:", b, c, d)
# If nothing reaches the target mark it as no triplet found
else:
    print("No triplet found")