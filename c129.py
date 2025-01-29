def BFS(y,x):
    q = [(y,x)]
    while len(q) > 0:
        y,x = q.pop(0)
        visited[y][x] = 1

        if y != n-1 and visited[y+1][x] == 0 and MAP[y+1][x] == '@':
            visited[y+1][x] = 1
            q.append((y+1,x))
        if y != 0 and visited[y-1][x] == 0 and MAP[y-1][x] == '@':
            visited[y-1][x] = 1
            q.append((y-1,x))
        if x != m-1 and visited[y][x+1] == 0 and MAP[y][x+1] == '@':
            visited[y][x+1] = 1
            q.append((y,x+1))
        if x != 0 and visited[y][x-1] == 0 and MAP[y][x-1] == '@':
            visited[y][x-1] = 1
            q.append((y,x-1))
        if y != n-1 and x != m-1 and visited[y+1][x+1] == 0 and MAP[y+1][x+1] == '@':
            visited[y+1][x+1] = 1
            q.append((y+1,x+1))
        if y != n-1 and x != 0 and visited[y+1][x-1] == 0 and MAP[y+1][x-1] == '@':
            visited[y+1][x-1] = 1
            q.append((y+1,x-1))
        if y != 0 and x != m-1 and visited[y-1][x+1] == 0 and MAP[y-1][x+1] == '@':
            visited[y-1][x+1] = 1
            q.append((y-1,x+1))
        if y != 0 and x != 0 and visited[y-1][x-1] == 0 and MAP[y-1][x-1] == '@':
            visited[y-1][x-1] = 1
            q.append((y-1,x-1))
while True:
    n,m = map(int, input().split())
    if m == 0 and n == 0:
        break
    MAP = []
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(n):
        MAP.append(list(input()))
    count = 0
    for i in range(n):
        for j in range(m):
            if MAP[i][j] == "@" and visited[i][j] == 0:
                BFS(i,j)
                count += 1
    print(count)
