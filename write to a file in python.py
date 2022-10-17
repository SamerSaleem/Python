from fileinput import close

#Following code will open the text file and use the function "a+" to add text to the file.
with open("C:\\Users\\samir.rafid\\Desktop\\text.txt", "a+") as readit:
    readit.write("Hellllllloooooooooooo")

#Following to adding the text above, we will use the "with function with the r option" to read the file text again.
with open("C:\\Users\\samir.rafid\\Desktop\\text.txt", "r") as readit:
    print(readit.read())
#readit.close() no need when we are using "with" function because with is context manager in python and will close the file automatically.
