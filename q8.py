''' m =Mass		d = Density 		v = Volume
// write a program that calculate Mass Volume and Density'''

print('Press 1 for Mass')
print('Press 2 for Density')
print('Press 3 for Volume')

x=int(input("Enter Your Choice : "))

if(x==1):  #Mass
    v=int(input("Enter Your Volume : "))
    d=int(input("Enter Your Density : "))
    print("Your Mass is : ",v*d)
elif(x==2): #density
    m=int(input("Enter Your Mass : "))
    v=int(input("Enter Your Volume : "))
    print("Your Density is : ",m/v)
elif(x==3): # Volume
    m=int(input("Enter Your Mass : "))
    d=int(input("Enter Your Density : "))
    print("Your Mass is : ",m*d)

else:
    print("You are print something Wrong")
