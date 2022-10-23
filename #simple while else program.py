#simple while else program
n = 5

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

i = range(4)

for num in i:
    print(num - 1)
else:
    print(num)

#the range below will print x starting from 0 and jumping by 3 every time but should be less than 10.
for x in range(0, 10, 3):
    print("x is equal", x)