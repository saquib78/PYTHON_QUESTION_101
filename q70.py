# generate fibonacci sequence using function

def fabri(num):
    f1 = f2 = 1
    print(f1,f2,end=' ')
    while num >2:
        y = f2
        f2 = f1+f2
        f1 = y
        print(f2,end='  ')
        num -=1
    print()



x = int(input('Enter Number of elemenet you wants : '))
fabri(x)