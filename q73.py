# find LCM  value using function

def LCM(num1,num2):
    num3 = num1*num2
    while num1 !=0 and num2 !=0:
        if num1 > num2:
            num1 %=num2
        else:
            num2 %=num1

    return num3 // (num1+num2)


x = int(input('Enter Your 1st Number : '))
y = int(input('Enter Your 2d Number : '))

print(f'LCM of Both Number Are : {LCM(x,y)}')