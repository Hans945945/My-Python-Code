def bfs(y, x, g):
    n = 1
    q = [(y, x)]
    while q:
        y, x = q.pop(0)
        for dy, dx in ((1,0), (-1,0), (0,1), (0,-1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < a and 0 <= nx < b:
                if nums[ny][nx] == g and visited[ny][nx] == 0:
                    n += 1
                    visited[ny][nx] = 1
                    q.append((ny, nx))
    return n
a,b = map(int, input().split())
nums = [input().split() for _ in range(a)]
visited = [[0]*b for _ in range(a)]
N = int(input())
for _ in range(N):
    h = input()
    max_n = 1
    for i in range(a):
        for j in range(b):
            if nums[i][j] == h and visited[i][j] == 0:
                visited[i][j] = 1
                max_n = max(max_n,bfs(i,j,h))
    print(max_n if max_n > 1 else 0)
