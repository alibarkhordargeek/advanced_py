from datetime import date
from datetime import datetime

class Date:
    d = date.today().strftime('%Y/%m/%d')
    
    def __init__(self, bd):
        self.bd = bd.split('/')
        self.d = Date.d.split('/')
    
    def age(self):
        tst = 0
        self.d.extend(self.bd)
        for i in range(0, len(self.d)):
            if self.d[i][0] == '0':
                self.d[i] = self.d[i][1:]
        for i in range(0, len(self.d)):
            self.d[i] = int(self.d[i])
        if self.d[4] > 12:
            print('WRONG')
            tst = 1
        elif self.d[5] > 31:
            print('WRONG')
            tst = 1
        if tst == 0:
            x = datetime(self.d[0], self.d[1], self.d[2])
            y = datetime(self.d[3], self.d[4], self.d[5])
            c = x - y
            ag = c.days // 365
            print(ag)

dt = input()
person = Date(dt)
person.age()
        
