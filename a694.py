import sys
data = sys.stdin.read().splitlines()
index = 0
r = []
while index < len(data):
    n,m = map(int, data[index].strip().split())
    if n == 0 and m == 0:
        break
    foods = [[0]*(n+1) for _ in range(n+1)]
    index += 1
    for i in range(1, n+1):
        row = list(map(int, data[index].strip().split()))
        index += 1
        for j in range(1, n+1):
            foods[i][j] = (row[j-1] + foods[i-1][j] + foods[i][j-1] - foods[i-1][j-1])
    for _ in range(m):
        y1, x1, y2, x2 = map(int, data[index].split())
        index += 1
        r.append(str(foods[y2][x2] - foods[y1-1][x2] - foods[y2][x1-1] + foods[y1-1][x1-1]))
sys.stdout.write("\n".join(r)+"\n")
