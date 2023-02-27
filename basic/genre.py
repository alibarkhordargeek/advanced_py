c = int(input())
cou = 0
genr = {'Adventure': 0, 'Comedy': 0, 'Horror': 0, 'History': 0, 'Romance': 0, 'Action': 0}
while cou < c:
    l = []
    mov = input()
    l = mov.split()
    for i in l:
        for j in list(genr.keys()):
            if i == j:
                genr[j] += 1
    cou += 1
l = list()
for i in genr:
    l.append([i, genr[i]])
for i in range(0, len(l)):
    for j in range(0, len(l)):
        if l[i][1] > l[j][1]:
            l[i], l[j] = l[j], l[i]
        elif l[i][1] == l[j][1]:
            if l[i][0] < l[j][0]:
                l[i], l[j] = l[j], l[i]
for i in l:
    print('%s : %i' %(i[0], i[1]))
