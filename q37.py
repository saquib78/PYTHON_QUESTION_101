# sorting of word a/c to length in a string

str = input('Enter Your string : ')
strspl = str.split()

leng = len(strspl)

for i in range(leng-1):
    for j in range(leng -1):
        if len(strspl[j]) > len(strspl[j+1]):
            strspl[j],strspl[j+1] = strspl[j+1], strspl[j]

print(' '.join(strspl))