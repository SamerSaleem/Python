my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 55  #this number will be checked if existing in the list above or not.
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find #found will be matching any number in the list compared with to_find.
    if found:  #this means if found became True then break the loop.
        break

if found:
    print("\n Element found at index", i)
else:
    print("\n absent")