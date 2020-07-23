# unpack matrix in one line...

mat=[[1,2,3],[4,5,6],[7,8,9]]

y = [it for row in mat for it in row]
print(y)