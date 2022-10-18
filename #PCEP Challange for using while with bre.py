#PCEP Challange for using while with break in a small program.
secret_word = str(input("Please enter the secret word: \n"))

while True:
    if secret_word == "cisco":
        print("Good, you are allowed to enter!")
        break
    if secret_word != "cisco":
        print ("Please enter the correct passcode.")
        secret_word = str(input("Please enter the secret word: \n"))


