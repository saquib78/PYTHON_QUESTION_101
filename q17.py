# creat table 1 to 25  using for loop

x=1
print('>>>>>table>>>>>>>>>>')
for x in range(1, 26):
    y = 1
    for y in range(1, 11):
        print("%4d" % (x*y), end=" ")

    print()