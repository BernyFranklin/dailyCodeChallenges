"""
Date: 26 May 2022
Problem: Given an array of integers, return a new array such that each element 
         at index i of the new array is the product of all the numbers in the 
         original array except the one at i. For example, if our input was 
         [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
         If our input was [3, 2, 1], the expected output would be [2, 3, 6]
"""

def multiples(list):
    oldList = list
    newList = []
    i = 0
    # Loop through values in list
    while (i < len(list)):
        total = 1
        print("Index: " + str(i))
        for item in oldList:
            # If at list[i] continue
            if (item == list[i]):
                continue 
            # Else total *= 
            else:
                total = total * item
        # Append total to new array
        newList.append(total)
        print(newList)
        i += 1

list = [1, 2, 3, 4, 5]

multiples(list)