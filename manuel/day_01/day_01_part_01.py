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
    print("usage: ./day_01_part_01.py input_file sum_of_pairs")
    exit(2)

list_nums = []
checked_nums = set()

# Read file into an array
for line in file:
    list_nums.append(int(line))

# Make sure to close what you open
file.close()

# Find the pairs that add up to the sum and exit
for num in list_nums:
    if sum - num in checked_nums:
        print((sum - num) * num)
        exit(0)
    checked_nums.add(num)

# If pair was not found exit with error
print("pairs not found")
exit(2)
