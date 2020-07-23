# find the Quadrant of a point , when it is giVen by user

x=int(input("Enetr Your x-axis : "))
y=int(input("Enter Your y-axis : "))

if(x>0 and y>0):
    print("You Are Present in 1st Quadrant ")
elif(x<0 and y>0):
    print("You Are Present in 2nd Quadrant ")
elif(x<0 and y>0):
    print("You Are Present in 2nd Quadrant ")
elif(x<0 and y<0):
    print("You Are Present in 3rd Quadrant ")
elif(x>0 and y<0):
    print("You Are Present in 4th Quadrant ")
elif(x==0 and y>0):
    print("You Are Present on +Ve y-axis  ")
elif(x==0 and y<0):
    print("You Are Present on -Ve y-axis ")
elif(x>0 and y==0):
    print("You Are Present on +Ve x-axis ")
elif(x<0 and y==0):
    print("You Are Present on -Ve x-axis ")
elif(x==0 and y==0):
    print("You Are Present on Origin ")