# find factorial using recursion

def facto(num):
    if num ==1:
        return 1
    val = 1
    val =((num)*facto(num-1))
    return val

x = int(input('Enter Your Number : '))
print(facto(x))