#how to check this point belogs to circle or not

x=int(input("Enter x value :  "))
y=int(input("Enter y value :  "))
r=int(input("Enter radius value :  "))

a=(x*x)+(y*y);
b=r*r;

if(a>b):
    print("Your Entered Value is outside the circle");
elif(a==b):
    print("Your Entered Value is on the circle")
elif(a<b):
    print("Your Entered Value is inside the circle")