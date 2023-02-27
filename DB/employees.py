import mysql.connector

l = list()

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='employee')
cursor = cnx.cursor()
query = 'select * from inf'
cursor.execute(query)
for (n, w, h) in cursor:
    l.append([n, w, h])
cnx.close()

for i in range(0, len(l)):
    for j in range(0, len(l)):
        if l[i][2] > l[j][2]:
            l[i], l[j] = l[j], l[i]
        elif l[i][2] == l[j][2]:
            if l[i][1] < l[j][1]:
                l[j], l[i] = l[i], l[j]
                
for i in l:
    print(i[0], i[2], i[1])
