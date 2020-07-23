# print ascii table list

for i in range(32,128): #this value is 'SPACE' to 'DEL'
    print(chr(i), end= ' ')
    if (i-1)%10==0:
        print()

print()