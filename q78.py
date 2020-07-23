# how to use read methode

fp = open('project_77_78_79_80.txt')
da = fp.read()
fp.close()

print(repr(da)) # it is print my statement in string their for new line use (\n)

da = da.split() # this make all word different . mens it split my data at ' '.
print(da)