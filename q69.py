# average of a list using function
def avge_list(fi):
    last = len(fi)
    sum = 0
    for i in fi:
        sum +=i
    return sum//i

x = input('enter your number (b/w two inter use " ") : ')
x=x.split()

for i in range(len(x)):
    x[i]=int(x[i])

ave = avge_list(x)

print(f'The Result of list average is : {ave}')