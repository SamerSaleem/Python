#lists-collecting data
#how to use lists and print positions inside the list.
numbers = [1, 3, 10, 11, 15]

print("Position 4 of the numbers list is: ", numbers[3]) #this will print position 4 
print("While the whole numbers list is : ", numbers) 

#change value inside a list
numbers[4] = 111
print('This is the updated list of numbers:', numbers)

numbers[2] = numbers[1]
print ('position 3 is now equals to position index "2" which is', numbers[2])
