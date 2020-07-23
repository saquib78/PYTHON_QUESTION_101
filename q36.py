# select the integer in a string

str = input('Enter Your Value : ')

lenstr = len(str)

num = []
x=0
while x < lenstr:
    num1 = ' '
    symb = str[x]

    while '0' <= symb <= '9':
        num1 += symb
        x +=1

        if x<lenstr:
            symb = str[x]

        else:
            break
    x +=1

    if num1 != " ":
        num.append(int(num1))

print(num)