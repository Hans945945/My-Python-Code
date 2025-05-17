m,n = map(int, input().split())
es = [input() for _ in range(m)]
T = list(input())
S = []
for e in es[::-1]:
    for w in e[::-1]:
        if w == "0":
            S.insert(0,T.pop())
        else:
            S.append(T.pop())
    if e.count("1") % 2 == 1:
        if n % 2 == 0:
            S = S[n//2:] + S[:n//2]
        else:
            S = S[n//2+1:] + [S[n//2]] + S[:n//2]
    T = S
    S = []
print("".join(T))
    
