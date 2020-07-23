# take input from user and and see it is triangle or not and its name ?

x=int(input("Enter first side of triangle length : "))
y=int(input("Enter second side of triangle length : "))
z=int(input("Enter third side of triangle length : "))

if(x+y>z or y+z>x or z+x>y):
    if(x==y and x==z):
        print("This is equilateral triangle")
    elif(x==y and x!=z or y==z and y!=x or z==x and z!=y):
        print("This is isosceles triangle")
    else:
        print("This is scalene triangle")
else:
    print("can't able to make triangle")