import sys
def BFS(y,x,c):
    visited[y][x] = 1
    q = [(y,x)]
    while q:
        y,x = q.pop(0)
        if y > 0 and MAP[y-1][x] == c and not visited[y-1][x]:
            visited[y-1][x] = 1
            q.append((y-1,x))
        if y < n-1 and MAP[y+1][x] == c and not visited[y+1][x]:
            visited[y+1][x] = 1
            q.append((y+1,x))
        if x > 0 and MAP[y][x-1] == c and not visited[y][x-1]:
            visited[y][x-1] = 1
            q.append((y,x-1))
        if x < n-1 and MAP[y][x+1] == c and not visited[y][x+1]:
            visited[y][x+1] = 1
            q.append((y,x+1))
    return
data = sys.stdin.readlines()
n = int(data.pop(0))
MAP = [s.split() for s in data]
visited = [[0]*n for _ in range(n)]
count = 0
for i in range(n):
    for j in range(n):
        if MAP[i][j] != "0" and not visited[i][j]:
            count += 1
            BFS(i,j,MAP[i][j])
print(count)
