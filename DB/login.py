import mysql.connector

tst = 0
stri = ['abcdefghijklmnopqrstuvwxyz']

un = input('Enter an email: ')

while True:
    if '@' in un:
        if '.' in un:
            break
        else:
            print('right input: expression@str.str')
            un = input('Enter an email: ')
    else:
        print('right input: expression@str.str')
        un = input('Enter an email: ')

while True:
    l = un.split('@')
    for i in l[0]:
        if i in stri[0]:
            tst = 1
    l2 = l[1].split('.')
    for i in l2[0]:
        if i not in stri[0]:
            tst = 0
    for i in l2[1]:
        if i not in stri[0]:
            tst = 0
    
    if tst == 1:
        break
    elif tst == 0:
        while True:
            print('right input: expression@str.str')
            un = input('Enter an email: ')
            if '@' in un:
                if '.' in un:
                    break
                else:
                    print('right input: expression@str.str')
                    un = input('Enter an email: ')
            else:
                print('right input: expression@str.str')
                un = input('Enter an email: ')

pw = input('Enter a password: ')

use = input('username for DB: ')
pas = input('password for DB: ')
hos = input('hostname: ')
db = input('database: ')
table = input('table: ')
cnx = mysql.connector.connect(user=use, password=pas,
                              host=hos,
                              database=db)
cursor = cnx.cursor()
cursor.execute('insert into %s values (\'%s\', \'%s\')' %(table, un, pw))
cnx.commit()
cnx.close()