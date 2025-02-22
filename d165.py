import sys
def BFS(y,x):
    total = 0
    visited[y][x] = 1
    q = [(y,x)]
    while q:
        y,x = q.pop(0)
        total += farm[y][x]
        
        if y > 0 and farm[y-1][x] > 0 and visited[y-1][x] == 0:
            visited[y-1][x] = 1
            q.append((y-1,x))
        if y < n-1 and farm[y+1][x] > 0 and visited[y+1][x] == 0:
            visited[y+1][x] = 1
            q.append((y+1,x))
        if x > 0 and farm[y][x-1] > 0 and visited[y][x-1] == 0:
            visited[y][x-1] = 1
            q.append((y,x-1))
        if x < m-1 and farm[y][x+1] > 0 and visited[y][x+1] == 0:
            visited[y][x+1] = 1
            q.append((y,x+1))
    return total
            
        
idx = 0
data = sys.stdin.readlines()
r = []
while idx < len(data):
    n,m = map(int, data[idx].split())
    farm = []
    for _ in range(n):
        idx += 1
        farm.append(list(map(int, data[idx].split())))
    idx += 1
    visited = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    biggest = float("-inf")
    for i in range(n):
        for j in range(m):
            if farm[i][j] > 0 and not visited[i][j]:
                count += 1
                biggest = max(biggest, BFS(i,j))
    r.append(count)
    r.append(biggest)
sys.stdout.write("\n".join(map(str, r))+"\n")
