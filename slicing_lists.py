list_1 = [1]
list_2 = list_1[:]  #this will make list take the value of the content of list 1 and won't get updated.
list_1[0]= 15
print ("the list2 value is", list_2) #will print original value which is 1. because we used slicing. in line 2.
print("the updated list1 is ", list_1)

a=[123]
b = a
a[0]= 1234
print("b value is", b)
print("a value is", a)
