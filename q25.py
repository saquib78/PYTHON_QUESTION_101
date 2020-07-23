# factorial using while loop

num = int(input('Enter Your Number : '))
numb = 1
while num >0:
    numb *=num
    num = num-1

print('Factorial Value is : ',numb)