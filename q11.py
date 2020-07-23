#how to check a leap year

yr=int(input("Enter your year : "));

if(yr%400==0):
    print("Your Entered year is Leap Year");
elif (yr % 100 == 0):
    print("Your Entered year is not Leap Year");
elif (yr % 4 == 0):
    print("Your Entered year is Leap Year");
else:
    print("Your Entered year is not Leap Year");