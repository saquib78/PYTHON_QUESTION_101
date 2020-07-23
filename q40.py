# Check it is palindrome or not

str = input('Enter Your String : ')

leng = len(str)

for i in range(leng//2):
    if str[i] !=str[-1-i]: # if we numbaring the word in string it is
                                # starts  with -i
        print('This is not a palindrome')
        quit()

print('This is palindrome')