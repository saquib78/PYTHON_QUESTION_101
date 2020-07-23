# find longest word in the string
str = input('Enter Your String : ')

first = str.split()
l=0
for i in range(1,len(first)):
    if len(first[l]) < len(first[i]):
        l = i

print(first[l])