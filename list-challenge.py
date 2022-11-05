# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append('john lennon')
beatles.append('paul mccartney')
beatles.append('george harrison')
print("Step 2:", beatles)

# step 3
for i in beatles:
    beatles.append(input('Please enter band members: '))
    beatles.append(input('Enter another name pls: '))
    break
print("Step 3:", beatles)

# step 4
del beatles[3]

print("Step 4:", beatles)
del beatles [3]
# step 5
beatles.insert(4, 'ringo')
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))