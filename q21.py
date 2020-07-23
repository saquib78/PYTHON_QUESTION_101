# sum and product of digits in an integer

num = abs(int(input('Enter Your Integer Value : ')))
s=0
m = 1
while num !=0:
    dig = num%10
    s += dig
    m *= dig
    num = num // 10

print('Sum is : ', s)

print('Product is : ', m)