# how reverse the order of word in string

def ord_rev(str):
    str = str.split()
    str.reverse()
    return ' '.join(str)

print(ord_rev(input('Insert Your string : ')))