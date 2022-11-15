#this small program shows the difference between lists and normal variable.
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print("list 2 is ", list_2) #it will print the updated value.
a=5
b=a
a=7
print(b) #it will print the original value.