#For-Else program
i = 111

#below range is not going to work, because 1 is less than 2, but if you change the value to 11 then it will show different output.
for i in range(2, 1):
    print(i)
#the else here will print the original value of i if the for loop couldn't print it as range.so this is the condition.
else:
    print("else:", i)

