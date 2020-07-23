# create table using while loop 1 to 20

x=1
y=1

while x < 11:
    y=1
    while y < 21:
        result = x*y
        # "%4d" is used to print tha data for human-readable.
        print("%4d" % result,end=" ")
        y=y+1

    print()
    x=x+1

