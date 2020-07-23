# find average of two number , using function

def avg(num1,num2):
    x = (num1+num2)/2
    return x

a = int(input('Enter 1st integer : '))

b = int(input('Enter 2nd element : '))

c = avg(a,b)
print(f'Average of both number is = {c}')