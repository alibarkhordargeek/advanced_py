cou = 0
mghD = dict()

while cou < 10:
    mgh = []
    mgh2 = []
    mgh3 = []
    num = int(input())
    for i in range(2, num+1):
        if num % i == 0:
            mgh.append(i)
    for i in mgh:
        for j in range(2, i):
            if i % j == 0:
                mgh2.append(i)
    for i in mgh:
        if i not in mgh2:
            mgh3.append(i)
    mghD[num] = len(mgh3)
    cou += 1

top = list()
for i in list(mghD.keys()):
    if mghD[i] == max(list(mghD.values())):
        top.append(i)
        c = mghD[i]
        
print(max(top), c)
                
