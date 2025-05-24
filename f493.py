def bfs(y,x):
    N = 1
    q = [(y,x)]
    while q:
        y,x = q.pop(0)
        if y > 0 and MAP[y-1][x] == "W" and visited[y-1][x] == 0:
            N += 1
            visited[y-1][x] = 1
            q.append((y-1,x))
        if y < n-1 and MAP[y+1][x] == "W" and visited[y+1][x] == 0:
            N += 1
            visited[y+1][x] = 1
            q.append((y+1,x))
        if x > 0 and MAP[y][x-1] == "W" and visited[y][x-1] == 0:
            N += 1
            visited[y][x-1] = 1
            q.append((y,x-1))
        if x < m-1 and MAP[y][x+1] == "W" and visited[y][x+1] == 0:
            N += 1
            visited[y][x+1] = 1
            q.append((y,x+1))
    return N
n,m = map(int, input().split())
MAP = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
max_n = 0
min_n = float("inf")
count = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and MAP[i][j] == "W":
            visited[i][j] = 1
            N = bfs(i,j)
            max_n = max(max_n,N)
            min_n = min(min_n,N)
            count += 1

print(max_n, min_n if max_n != 0 else 0, count)

