#The comparison constant is configured below:
largest_number = -99999999

counter = 0

#the while true means keep doing the loop without any condition until user enters the -1 which will break the loop.
#if you dont use if/break sentence here, then you will need to add the condition with same line as "while".
while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

