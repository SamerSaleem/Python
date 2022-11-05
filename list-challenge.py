# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append('john lennon')
beatles.append('paul mccartney')
beatles.append('george harrison')
print("Step 2:", beatles)

# step 3
for i in range(2):  #this 2 in the range will run the loop two times only.
    beatles.append(input('Please enter band members: '))
    
    
print("Step 3:", beatles)

# step 4
del beatles[-1]

print("Step 4:", beatles)
del beatles[-1]
# step 5
beatles.insert(4, 'ringo')
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))