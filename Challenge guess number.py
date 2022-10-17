secret_number = 777
#below is called Multiline printing....
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
new_guess = int(input("please enter your guess:"))
while new_guess != secret_number:
    print("Guess again")
    new_guess=int(input("Please enter your guess: "))
if new_guess == secret_number:
    print("Bingo")


    