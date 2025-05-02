import sys
data = sys.stdin.readlines()
n,m,q = map(int, data.pop(0).split())
C = []
for i in range(n):
    C.append(list(map(int, data[i].split())))
    
table = {}
for i in range(n):
    for j in range(m):
        table[C[i][j]] = (i,j)

r = []
for k in range(q):
    i,j = table[int(data[n+k])]
    r.append(" ".join(map(str, sorted([C[i-1][j], C[i][j-1], C[(i+1)%n][j], C[i][(j+1)%m]]))))
sys.stdout.write("\n".join(r)+"\n")

    
