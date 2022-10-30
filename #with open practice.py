#with open practice
with open ('parsing.csv') as excel: #open and then read it with read
    print(excel.read())

with open ('parsing.csv', 'a+') as excel:   #this will append to the end of the file
    excel.write('Wireless\n')
    
