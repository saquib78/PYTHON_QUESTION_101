# simple thermometer

x=int(input("Press 1 for Celsius and 2 for Fahrenheit : "))

if(x==1):
    y=int(input('Enter your value in Celsius : '));
    print("Your value in  is  Fahrenheit :  ",((y*9)/5)+32);
elif(x==2):
    z=int(input("Enter your value in Fahrenheit : "))
    print("Your value in Celsius : ",(z-32)*5/9);
else:
    print("you are Press some Wrong Button")