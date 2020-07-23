# detect it have valid file extension or not or present or
# not present

valid = ['gif','jpg','jpge','png','txt','xmls']

inp = input('Enter file name with extension : ').split('.')

if len(inp) >= 2:
    ext = inp[-1].lower()

    if ext in valid:
        print('File extension exits')
    else:
        print('File extension does not exist')

else:
    print('File does not have extension')