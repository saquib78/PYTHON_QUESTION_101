# use class and constructor.

class company:
    def __init__(self,empl_first,empl_surn):
        self.first =empl_first
        self.sur = empl_surn

    def empl(self):
        return self.first+ ' '+self.sur

staff = []

for i in range(2):
    name = input('Enter Your First Name and Surname : ')
    name = name.split()
    staff.append(company(name[0],name[1]))

for i in staff:
    print(i.empl())