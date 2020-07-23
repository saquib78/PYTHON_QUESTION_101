# take two number if it is divisible by then print it is wrong.
# otherwise print value

a= float(input('Enter Your First number : '))
b = float(input('Enter Your Second Number : '))

try:
    c = a/b

except ZeroDivisionError:
    print('You are Enter 0 so value goes to infinite')

else:
    print(c)