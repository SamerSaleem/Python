#this script, will make the while loop to keep printing number subtracted by 1 until the result is equal to 0 then it will stop.
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

#on the otherhand, this is how to make incremental counter which is the opposite of the code above.
inc_counter= 0
while inc_counter !=5:
    print("Inside the loop.  ", inc_counter)
    inc_counter +=1
print("Outside the loop", inc_counter)