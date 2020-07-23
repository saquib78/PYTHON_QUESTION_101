# this is additional problem ==> find the Quadrant when angle is given by user.

x=int(input("Enter Your angle in degree : "))
if(x>0 and x<90):
    print("You are in 1st Quadrant")
elif(x>90 and x<180):
    print("You are in 2nd Quadrant")
elif(x>180 and x<270):
    print("You are in 3rd Quadrant")
elif(x>270 and x<360):
    print("You are in 4th Quadrant")