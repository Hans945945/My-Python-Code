import sys
r,c = map(int, sys.stdin.readline().split())
table = [[0 for _ in range(c+2)]]
table.extend([[0] + s.split() + [0] for s in sys.stdin.read().splitlines()])
table.append([0 for _ in range(c+2)])
count = 0
for i in range(1, r+1):
    for j in range(1, c+1):
        here = table[i][j]
        if table[i][j+1] != here and table[i][j-1] != here and table[i+1][j] != here and table[i-1][j] != here and table[i-1][j+1] != here and table[i+1][j+1] != here and table[i+1][j-1] != here and table[i-1][j-1] != here:
            count += 1
print(count)
