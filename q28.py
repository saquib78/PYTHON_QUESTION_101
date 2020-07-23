# how to get get fibonacci value

x = int(input('Enter your series position : '))

a=1
b=1

for i in range(x-2):
    result = a+b
    a=b
    b=result

print(result)