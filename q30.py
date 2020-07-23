# find maximum one digit number present in an integer . EX 12321 have maximum is 3.

num = int(input('Enter Your Number : '))
digits = 0
max = 0
while num > 0:
    digits = num%10

    if digits > max:
        max = digits

    num = num//10

print('Max Element present is : ',max)