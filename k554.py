import sys
data = sys.stdin.readlines()
n,m = map(int, data[0].split())
MAP = []
for s in data[1:]:
    MAP.append(list(map(int, s.split())))
r = [[0]*(m+2) for _ in range(n+2)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if MAP[i-1][j-1] == 1:
            r[i][j] += 1
            r[i+1][j] += 1
            r[i][j+1] += 1
            r[i-1][j] += 1
            r[i][j-1] += 1
        elif MAP[i-1][j-1] == 2:
            r[i][j] += 1
            for k in range(j+1,m+1):
                r[i][k] += 1
            for k in range(1,j):
                r[i][k] += 1
            for k in range(i+1,n+1):
                r[k][j] += 1
            for k in range(1,i):
                r[k][j] += 1
sys.stdout.write("\n".join(" ".join(map(str, row[1:-1])) for row in r[1:-1])+"\n")
            
            
