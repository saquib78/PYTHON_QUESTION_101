# make a program that find greatest number using if else condition

x=int(input("Enter Your First Number : "))
y=int(input("Enter Your Second Number : "))
z=int(input("Enter Your Third Number : "))

if(x>y and x>z):
    print("Your First Number is Greatest ")
elif(y>x and y>z):
    print("Your Second Number is Greatest")
elif(z>y and z>x):
    print("Your Third Number is Greatest")