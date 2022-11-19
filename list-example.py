my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0] #define the largest number as position 0 in the list above.

for i in my_list: #define the letter i as any of the numbers in the list
    if i > largest:  #condition if any of the numbers was bigger than the current largest number then print it!
        largest = i

print(largest)

