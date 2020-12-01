#!/usr/bin/env python3
#
# Manuel Nila - Dec. 2020

# Using sys to access cmd line arguments
import sys

# Open the file and ensure good arguments
try:
    sum = int(sys.argv[2])
    file = open(str(sys.argv[1]), "r")
except IOError:
    print("input file doesn't exist")
    exit(2)
except:
    print("usage: ./day_01_part_02.py input_file sum_of_triplet")
    exit(2)

list_nums = []
checked_nums = set()

# Read file into an array
for line in file:
    list_nums.append(int(line))

# Make sure to close what you open
file.close()

# Find the pairs that add up to the sum and exit
for index, num1 in enumerate(list_nums):
    for num2 in list_nums[index:]:
        if sum - num1 - num2 in checked_nums:
            print((sum - num1 - num2) * num1 * num2)
            exit(0)
        checked_nums.add(num2)
    checked_nums.add(num1)

# If triplet was not found exit with error
print("triplet not found")
exit(2)
