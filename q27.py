# fibonacci sequence

x = int(input('Enter Your sequence length : '))

a = 1
b = 1
print(a,b,end=' ')
for i in range(x-2):
    result = a+b
    print(result, end=' ')
    a = b
    b = result