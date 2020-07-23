# count no of digits in an integer. Example 123 have 3 digits

num = int(input('Enter your Integer : '))
c=0
while num > 0:
    num = num//10
    ''' '//' this is floor division .
    we use here because if i am divide a number by 10. then after it is also lai b/w 0 to 1
    . and this is effect my program '''
    c=c+1

print('Number of digits : ',c)