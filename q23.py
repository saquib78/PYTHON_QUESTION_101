# sum of n-series in of an element

a = int(input('Enter Your First Number : '))
d = int(input('Enter difference b/w to number : '))
n = int(input('Enter number of terms : '))

result = (n/2)*(2*a+((n-1)*d))

print('The Value is : ',result)
