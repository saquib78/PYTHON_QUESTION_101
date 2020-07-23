# write a file from here

fp = open('project_81.txt','w')

fp.write('Hii I m abdul malik\n')
fp.write('This is comes from program\n')
value = ['This is first .\n','this is second .\n','this is third.']
fp.writelines(value)
fp.close()

dp = open('project_81.txt')
print(dp.read())
dp.close()