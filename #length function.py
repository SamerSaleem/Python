#length function
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList length:", len(numbers))  # Printing the list's length.

del numbers [0]  #deleting a number from the list.
print('Removing one of the numbers of this list is in progress...\n') #comment for explanation. 
print ('the new length is', len(numbers))
