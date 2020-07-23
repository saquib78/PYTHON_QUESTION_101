# how to remove symbol from text

symb = ['.',',','@',';',':','!','?','(',')']

str1 = input('Enter Your String : ')
listitem = str1.split()

x=0

for i in listitem:
    if i[-1] in symb:
        listitem[x]=i[:-1]
        i = listitem[x]
    if i[0] in symb:
        listitem[x] = i[1:]

    x +=1

x = 0
while x < len(listitem):
    print(listitem[x],end=' ')
    x +=1
    if x%5 == 0:
        print()