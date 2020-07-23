# how to rise exception.

list_1 = ['a','b','c','d','e','f','g','h']

alp = input("Enter Your letter : ")

if alp in list_1:
    print(1)

else:
    raise ValueError("Letter does not present") # this is showing your message
                                                #when program get error.