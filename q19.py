# make a simple calculetor

x = int(input('Enter Your First Number : '))
y= int(input('Enter Your Second Number : '))

print('+,-,*,/,%')
sym = input('Enter Your operator (that is mention above) : ')


if sym == '+':
    print('Sum is = ',x+y)
elif sym == '-':
    print('Substrate = ',x-y)
elif sym == '*':
    print('Multiply is : ',x*y)
elif sym == '/':
    print('Quotient is : ',x/y)
elif sym == '%':
    print('Reminder is : ',x%y)
else:
    print('You are press some wrong key ! do it  again')