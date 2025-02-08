N,M,L,Q = map(int, input().split())
f = []
t = []
bad = []
for _ in range(M):
    a,b = map(int, input().split())
    f.append(a)
    t.append(b)
for _ in range(L):
    temp = int(input())
    bad.append(temp)
    while f.count(temp)!= 0 and bad.count(t[f.index(temp)]) == 0:
        bad.append(t[f.index(temp)])
        t.pop(f.index(temp))
        f.pop(f.index(temp))
for i in range(L,len(bad)):
    temp = bad[i]
    while f.count(temp)!= 0 and bad.count(t[f.index(temp)]) == 0:
        bad.append(t[f.index(temp)])
        t.pop(f.index(temp))
        f.pop(f.index(temp))
for _ in range(Q):
    s = int(input())
    if bad.count(s) == 0:
        print("Ya~~")
    else:
        print("TUIHUOOOOOO")
            
