# find the fibonacci value using recursion
#1 1 2 3 5 8 13 21.........

def fabi(num):
    if num == 1 or num == 2:
        return 1
    return fabi(num-1) + fabi(num-2)

val = int(input('Enter position.that fibonacci value you wants : '))
print(fabi(val))