class Kelas:
    def __init__(self, sen, ghad, vazn):
        self.sen = sen
        self.vazn = vazn
        self.ghad = ghad
    def msen(self):
        return (sum(self.sen)/len(self.sen))
    def mghad(self):
        return (sum(self.ghad)/len(self.ghad))
    def mvazn(self):
        return (sum(self.vazn)/len(self.vazn))

c = 0
while c < 2:
    t = input()
    s = input()
    s = s.split()
    for i in range(0, len(s)):
        s[i] = int(s[i])
    gh = input()
    gh = gh.split()
    for i in range(0, len(gh)):
        gh[i] = int(gh[i])
    v = input()
    v = v.split()
    for i in range(0, len(v)):
        v[i] = int(v[i])
    if c == 0:
        A = Kelas(s, gh, v)
    elif c == 1:
        B = Kelas(s, gh, v)
    c += 1

c = 0
while c < 2:
    if c == 0:
        print(A.msen())
        print(A.mghad())
        print(A.mvazn())
    elif c == 1:
        print(B.msen())
        print(B.mghad())
        print(B.mvazn())
    c += 1

agh = A.mghad()
bgh = B.mghad()
av = A.mvazn()
bv = B.mvazn()
if agh > bgh:
    print('A')
elif bgh > agh:
    print('B')
elif agh == bgh:
    if av < bv:
        print('A')
    elif bv < av:
        print('B')
    elif av == bv:
        print('Same')
