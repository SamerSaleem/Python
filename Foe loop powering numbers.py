power = 1
#the loop below will continue from 0 to 15 and will keep multiplying the numbers 2^0 then 2^1 then 2^2 ...etc 2^15 
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2
