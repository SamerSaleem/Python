#nested condition
a = 15
if a == 15:
    if (a + 5) ==21:
        print("it is Correct")
    else:
        print("are you idiot?")
else:
    print("No Hi to you!")

b=123
if a==b:
    print("A is same as A")
elif a != b:
    print("No A is not equal to B")

elif a == 15:
    print("A is equal to 15")
else:
    print("play some football")

#The way to assemble subsequent if-elif-else statements is sometimes called a cascade.

#Notice again how the indentation improves the readability of the code.

#Some additional attention has to be paid in this case:

#you mustn't use else without a preceding if;
#else is always the last branch of the cascade, regardless of whether you've used elif or not;
#else is an optional part of the cascade, and may be omitted;
#if there is an else branch in the cascade, only one of all the branches is executed;
#if there is no else branch, it's possible that none of the available branches is executed.
