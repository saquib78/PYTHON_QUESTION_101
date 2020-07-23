# how to create a quaderic equaion and its roots

x=int(input("Enter x value :  "))
y=int(input("Enter y value :  "))
z=int(input("Enter z value :  "))

a=(y*y)-4*x*z;

if(a>0):
    print("There are two real roots");

elif(a==0):
    print("There is only one real roots");

elif(a<0):
    print("There are no real roots");