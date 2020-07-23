# how to use read line methode

ed = open('project_77_78_79_80.txt')
da = []

i = ed.readline()

while i !='':
    da.append(i)
    i=ed.readline()

ed.close()
print(da)