cou = int(input())
c = 0
li = list()

while c < cou:
    nms = input()
    l = nms.split('.')
    li.append(l)
    c += 1

for i in range(0, len(li)):
    li[i][1] = li[i][1][0].upper() + li[i][1][1:].lower()
for i in range(0, len(li)):
    for k in range(0, len(li)):
        if li[i][0] == 'f':
            if li[k][0] == 'm':
                li[i], li[k] = li[k], li[i]
        if li[i][0] == li[k][0]:
            if li[i][1] < li[k][1]:
                li[i], li[k] = li[k], li[i]

for each in li:
    print('%s %s %s' %(each[0], each[1], each[2]))

