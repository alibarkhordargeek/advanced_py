pr = input()
l = pr.split()
l2 = list()
for i in range(1, len(l)):
    if type(l[i]) != int:
        if l[i-1][len(l[i-1])-1] != '.':
            if l[i][0] == l[i][0].upper():
                l2.append([i+1, l[i]])
for i in range(0, len(l2)):
    if l2[i][1][len(l2[i][1])-1] == '.':
        l2[i][1] = l2[i][1][:len(l2[i][1])-1]
    elif l2[i][1][len(l2[i][1])-1] == ',':
        l2[i][1] = l2[i][1][:len(l2[i][1])-1]
        
for i in l2:
        print('%i:%s' %(i[0], i[1]))
if len(l2) == 0:
        print('None')
                
