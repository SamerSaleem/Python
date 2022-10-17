#if you want to execute more than one statement inside one while, you must (as with if) indent all the instructions in the same way;
#an instruction or set of instructions executed inside the while loop is called the loop's body;
#if the condition is False (equal to zero) as early as when it is tested for the first time, the body 
#is not executed even once (note the analogy of not having to do anything if there is nothing to do);
#the body should be able to change the condition's value, 
#because if the condition is True at the beginning, the body might run continuously to infinity - 
#notice that doing a thing usually decreases the number of things to do).

# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.note the indentiation which means you will keep entering the number variable until you enter -1 to break it.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

