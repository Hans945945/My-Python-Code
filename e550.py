import sys
def bfs(y, x):
    N = 1
    q = [(y, x)]
    visited[y][x] = 1
    while q:
        y, x = q.pop(0)
        if y > 0 and MAP[y-1][x] == "0" and visited[y-1][x] == 0:
            N += 1
            visited[y-1][x] = 1
            q.append((y-1, x))
        if y < n-1 and MAP[y+1][x] == "0" and visited[y+1][x] == 0:
            N += 1
            visited[y+1][x] = 1
            q.append((y+1, x))
        if x > 0 and MAP[y][x-1] == "0" and visited[y][x-1] == 0:
            N += 1
            visited[y][x-1] = 1
            q.append((y, x-1))
        if x < m-1 and MAP[y][x+1] == "0" and visited[y][x+1] == 0:
            N += 1
            visited[y][x+1] = 1
            q.append((y, x+1))
    return N

data = [s.strip() for s in sys.stdin]
T = int(data[0])
idx = 1
r = []

for _ in range(T):
    idx += 1
    i, j = map(int, data[idx].split())
    idx += 1
    MAP = []
    while idx < len(data) and data[idx] != "":
        MAP.append(list(data[idx]))
        idx += 1
    n = len(MAP)
    m = len(MAP[0])
    visited = [[0]*m for _ in range(n)]
    if MAP[i-1][j-1] == "0":
        r.append(str(bfs(i-1, j-1)))
    else:
        r.append("0")

print("\n\n".join(r))
