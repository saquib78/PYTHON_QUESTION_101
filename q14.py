# produce a rendom numbr and then take input and show it is greater or not

import random


c = random.random() * 100;

a=round(c)
print(a)
while True:
    b = int(input("Enter Your Value :  "))

    if b == a:
        print("Your Entered Value is Equal to Random Number")
        break;
    elif b > a:
        print("Your Entered Value is greater then Random Number")
    elif b < a:
        print("Your Entered Value is less then Random Number")
