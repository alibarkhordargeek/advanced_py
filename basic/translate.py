cou = int(input())
c = 0
trns = dict()
while c < cou:
    w = []
    trn = input()
    w = trn.split()
    trns[w[1]] = w[0]
    trns[w[2]] = w[0]
    trns[w[3]] = w[0]
    c += 1
sent = input()
s = sent.split()
for i in range(0, len(s)):
    if s[i] in list(trns.keys()):
        s[i] = trns[s[i]]
print(' '.join(s))

    
    
