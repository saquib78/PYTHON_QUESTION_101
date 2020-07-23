# find greatest common divisor

x= int(input('Enter your first value : '))
y= int(input('Enter your second value : '))

while x!=0 and y!=0:
    if x>y:
        x %=y
    else:
        y &=x

gcd = x+y
print('Greatest Common Factor is : ',gcd)
