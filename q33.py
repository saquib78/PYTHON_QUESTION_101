# reverse the integer value

num = int(input('Enter Your Number : '))
x = num
mun = 0

while num > 0:
    digit = num%10
    num = num //10

    mun = mun*10
    mun = mun+digit

print(f'The reverse number of {x} is {mun}')
