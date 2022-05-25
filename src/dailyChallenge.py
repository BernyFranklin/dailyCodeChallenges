"""
Date: 25 May 2022
Problem: Given a list of numbers and a number k, 
         return whether any two numbers from the list add up to k.
         For example, given [10, 15, 3, 7] and k of 17, 
         return true since 10 + 7 is 17
"""

# List variable to send to function
l = [10, 15, 3, 7]
# Number given for comparison
k = 17

def addUp(l, k):
    # Import variables
    list = l
    answer = k
    # Initialize count for loop
    count = 0
    # Iterate through each value in list
    while (count < len(l)):
        # Initialize index for loop
        index = 0
        # Iterate through each value in list for each value in list
        while (index < len(l)):
            # If the index and count are equal, don't do anything.
            if (count != index):
                # If adding of two index == k return True
                if (answer == (list[count] + list[index])):
                    return True
            # Increment
            index += 1
        #Increment
        count += 1
    # No luck
    return False
        

print(addUp(l, k))