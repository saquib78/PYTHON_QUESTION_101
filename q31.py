# find complex and prime number
import math
num = int(input('Enter Your Number : '))

if num <2:
    print('Please insert again')
    quit()

elif num == 2:
    print('It is prime number')
    quit()

num1 = 2

num2 = int(math.sqrt(num))

while num1 <= num2:
    if num%num1 == 0:
        print('This is complex number')
        quit()
    num1 +=1

print('This is prime number')