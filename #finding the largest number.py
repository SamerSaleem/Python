#finding the largest number

num1=int(input("Please input your 1st number: "))
num2=int(input("Please input your 2nd number: "))
num3=int(input("Please input your 3rd number: "))

largest_num= max(num1, num2, num3)
#max is a built in function used by python to find the maximum value between variables
mini_num= min(num1, num2, num3)
print ("THe largest number is " , largest_num)

#min is a built-in function just like max function
print ("The smallest number is: ", mini_num)

