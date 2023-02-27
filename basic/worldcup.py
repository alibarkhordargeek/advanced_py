ir = {'w': 0, 'l': 0, 'd': 0, 'g': 0, 'p': 0}
sp = {'w': 0, 'l': 0, 'd': 0, 'g': 0, 'p': 0}
mor = {'w': 0, 'l': 0, 'd': 0, 'g': 0, 'p': 0}
por = {'w': 0, 'l': 0, 'd': 0, 'g': 0, 'p': 0}
li = list()
res = input()
l = res.split('-')
ir['g'] += (int(l[0]) - int(l[1]))
sp['g'] += (int(l[1]) - int(l[0]))
if l[0] > l[1]:
    ir['w'] += 1
    sp['l'] += 1
elif l[1] > l[0]:
    ir['l'] += 1
    sp['w'] += 1
else:
    ir['d'] += 1
    sp['d'] += 1
res = input()
l = res.split('-')
ir['g'] += (int(l[0]) - int(l[1]))
por['g'] += (int(l[1]) - int(l[0]))
if l[0] > l[1]:
    ir['w'] += 1
    por['l'] += 1
elif l[1] > l[0]:
    ir['l'] += 1
    por['w'] += 1
else:
    ir['d'] += 1
    por['d'] += 1
res = input()
l = res.split('-')
ir['g'] += (int(l[0]) - int(l[1]))
mor['g'] += (int(l[1]) - int(l[0]))
if l[0] > l[1]:
    ir['w'] += 1
    mor['l'] += 1
elif l[1] > l[0]:
    ir['l'] += 1
    mor['w'] += 1
else:
    ir['d'] += 1
    mor['d'] += 1
res = input()
l = res.split('-')
sp['g'] += (int(l[0]) - int(l[1]))
por['g'] += (int(l[1]) - int(l[0]))
if l[0] > l[1]:
    sp['w'] += 1
    por['l'] += 1
elif l[1] > l[0]:
    sp['l'] += 1
    por['w'] += 1
else:
    sp['d'] += 1
    por['d'] += 1
res = input()
l = res.split('-')
sp['g'] += (int(l[0]) - int(l[1]))
mor['g'] += (int(l[1]) - int(l[0]))
if l[0] > l[1]:
    sp['w'] += 1
    mor['l'] += 1
elif l[1] > l[0]:
    sp['l'] += 1
    mor['w'] += 1
else:
    sp['d'] += 1
    mor['d'] += 1
res = input()
l = res.split('-')
por['g'] += (int(l[0]) - int(l[1]))
mor['g'] += (int(l[1]) - int(l[0]))
if l[0] > l[1]:
    por['w'] += 1
    mor['l'] += 1
elif l[1] > l[0]:
    por['l'] += 1
    mor['w'] += 1
else:
    por['d'] += 1
    mor['d'] += 1
ir['p'] += (ir['w']*3) + ir['d']
sp['p'] += (sp['w']*3) + sp['d']
mor['p'] += (mor['w']*3) + mor['d']
por['p'] += (por['w']*3) + por['d']

li.append(['Iran', ir['w'], ir['l'], ir['d'], ir['g'], ir['p']])
li.append(['Spain', sp['w'], sp['l'], sp['d'], sp['g'], sp['p']])
li.append(['Morocco', mor['w'], mor['l'], mor['d'], mor['g'], mor['p']])
li.append(['Portugal', por['w'], por['l'], por['d'], por['g'], por['p']])
for i in range(0, len(li)):
    for j in range(0, len(li)):
        if li[i][5] > li[j][5]:
            li[i], li[j] = li[j], li[i]
        elif li[i][5] == li[j][5]:
            if li[i][1] > li[j][1]:
                li[i], li[j] = li[j], li[i]
            elif li[i][1] == li[j][1]:
                if li[i][0] < li[j][0]:
                    li[i], li[j] = li[j], li[i]
for i in li:
    print('%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' %(i[0], i[1], i[2], i[3], i[4], i[5]))

    



    
