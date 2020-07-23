# get factorial using for loop

num = int(input('Enter Your Number : '))
numb = 1

for x in range(num):
    numb *=num
    num = num-1

print('Factorial Value is : ',numb)