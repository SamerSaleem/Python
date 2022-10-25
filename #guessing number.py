#guessing number
import random

secretnumber = random.randint(1, 20)
print ("I'm thinking of a number between 1 and 20")

for guesstaking in range (1, 7):
    print('take a guess')
    guess = int(input())
    if guess < secretnumber:
        print('your guess is too low')
    elif guess > secretnumber:
        print('your guess is too high')
    else:
        break   #this condition is the correct guess and will break the loop.

if guess == secretnumber:
    print ('Good job! your guessed my number in! ' + str(guesstaking) + ' guesses')
else:
    print('nope, the number i was thinking about was ' + str(secretnumber))

    