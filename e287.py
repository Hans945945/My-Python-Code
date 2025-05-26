n,m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
y,x = 0,0
min_n = float('inf')
for i in range(n):
    for j in range(m):
        if min_n > nums[i][j]:
            min_n = nums[i][j]
            y,x = i,j
visited = [[0]*m for _ in range(n)]
total = min_n
while 1:
    visited[y][x] = 1
    min_n = float('inf')
    dx,dy = -1,-1
    if x < m-1 and visited[y][x+1] == 0:
        if min_n > nums[y][x+1]:
            min_n = nums[y][x+1]
            dy,dx = y,x+1
    if x > 0 and visited[y][x-1] == 0:
        if min_n > nums[y][x-1]:
            min_n = nums[y][x-1]
            dy,dx = y,x-1
    if y < n-1 and visited[y+1][x] == 0:
        if min_n > nums[y+1][x]:
            min_n = nums[y+1][x]
            dy,dx = y+1,x
    if y > 0 and visited[y-1][x] == 0:
        if min_n > nums[y-1][x]:
            min_n = nums[y-1][x]
            dy,dx = y-1,x
    if dx == -1 and dy == -1:
        print(total)
        break
    visited[dy][dx] = 1
    total += min_n
    y,x = dy,dx
    
