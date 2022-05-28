"""
Date: 28 May 2022
Problem: Given an array of integers, find the first missing positive integer in 
         linear time and constant space. In other words, find the lowest positive 
         integer that does not exist in the array. The array can contain duplicates 
         and negative numbers as well. For example, the input [3, 4, -1, 1] should 
         give 2. The input [1, 2, 0] should give 3
"""

def findLowestMissing(list):
    # Initialize  a counter
    count = 0
    # Iterate through values in array
    for r in list:
        # Start the counter
        count += 1
        # If the counter isn't in the array print what the count is
        if count not in list:
            print("First missing integer is " + str(count))
        # Keep looking
        else:
            continue

list = [1, 2, 0]

findLowestMissing(list)