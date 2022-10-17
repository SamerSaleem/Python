from fileinput import close


with open("C:\\Users\\samir.rafid\\Desktop\\VG1.txt", "r") as readit:
    print (readit.read())

#readit.close() no need whenwe are using with function because with is context manager in python and will close the file automatically.