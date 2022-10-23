#Pyramid challenge.this challenge is making program that prints the number of layers
#when you enter the number of the blocks, the while loop will do the following:
#as long as the layers is less than blocks, do the following
#give the height increment of 1
#remove a number from the block
#increment the layers by 1
#print the new height.

blocks = int(input("Please enter the number of blocks"))
height = 0
layers = 1
while layers <= blocks:
    height +=1
    blocks -= layers
    layers += 1
print ("The height of the pyramid is", height)
