#adding to list using for loop.
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)   #this will make the code add to list from the range of the loop

print(my_list)

my_list = [1, 2, 3, 4]
total = 0

for x in my_list:
    total += x
print('your total is', total)
