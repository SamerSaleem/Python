#Lists challenge
# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
from dataclasses import replace


my_numbers = [1, 2, 3, 4, 5]
print('please replace the middle number with an integer: ')
my_numbers[2]= int(input('Please enter new number: '))
print(my_numbers)
# Step 2: write a line of code that removes the last element from the list.
print('now we are going to remove the last number...')
del my_numbers[-1]
print(my_numbers)

#print the length of the list
print ('the length of the list is', len(my_numbers))


