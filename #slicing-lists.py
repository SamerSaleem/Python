#slicing
#list slicing is like => my_list[start:end]
'''start is the index of the first element included in the slice;
end is the index of the first element not included in the slice.'''

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]  #this slice will remove 10 and 2 from the new_list
print(new_list)

new2=my_list[ :3] #this will slice the list and print 1,2,3 positions
print(new2)

#reminder we use the slicing because lists are immutable. slice is like copy to same list.

new3=my_list[0:4] #this line and the next one are the same.
print(new3)

new4=my_list[:4] #this line and the next one are the same.
print (new4)

new5=my_list[2:len(my_list)]  #this means print from 3rd position to the number of the length of the list.
print (new5)
