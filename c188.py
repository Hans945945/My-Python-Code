import sys
P = [0] * 201
P[0] = 1  
for i in range(1, 201):
    for j in range(i, 201):
        P[j] += P[j - i]
r = []
for s in sys.stdin.readlines():
    r.append(P[int(s)])
sys.stdout.write("\n".join(map(str, r))+"\n")

