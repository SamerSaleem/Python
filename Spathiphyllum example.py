#this code should check the input from the user for the name of the word, if the word was Spathiphyllum then it will print the best plant ever, if it was in small letters
#it will print another input to correct user mistake
#if it was any other word then it will print "I want a Spathiphyllum now message "
plant= str(input("what is the word of the day?"))

if plant == "Spathiphyllum":
    print(" Spathiphyllum is the best plant ever!!")
elif plant == "spathiphyllum":
    print(" Spathiphyllum! not ", plant)
else:
    print("I want a Spathiphyllum Plant now!")




