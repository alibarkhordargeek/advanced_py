import re
tst = 0
ex = ['abcdefghijklmnopqrstuvwxyz0912345678']
s = ['abcdefghijklmnopqrstuvwxyz']
e = input()
res = re.findall(r'(\w+)\@(\w+)\.(\w+)', e)
if res == []:
    print('WRONG')
else:
    t = 0
    res = res[0]
    for ln in res[0]:
        if ln in ex[0]:
            if ln in s[0]:
                t = 1
            else:
                pass
        else:
           tst = 1 
    if t == 1:
        for l in res[1]:
            if l in s[0]:
                pass
            else:
                tst = 1
        for l in res[2]:
            if l in s[0]:
                pass
            else:
                tst = 1
        if tst == 0:
            print('OK')
        else:
            print('WRONG')
    else:
        print('WRONG')
