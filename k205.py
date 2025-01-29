import sys
Map = sys.stdin.read().splitlines()
n,m = map(int, Map.pop(0).split())
Map = [i.strip() for i in Map]
r = [list(row) for row in Map]
for i in range(n):
    for j in range(m):
        now = Map[i][j]
        if now.isdigit():
            count = 0
            visited = []
            if j < m-1 and Map[i][j+1] == "#":
                count += 1
                visited.append((i, j+1))
            if j > 0 and Map[i][j-1] == "#":
                count += 1
                visited.append((i, j-1))
            if i < n-1 and Map[i+1][j] == "#":
                count += 1
                visited.append((i+1, j))
            if i > 0 and Map[i-1][j] == "#":
                count += 1
                visited.append((i-1, j))
            if i > 0 and j < m-1 and Map[i-1][j+1] == "#":
                count += 1
                visited.append((i-1, j+1))
            if i < n-1 and j > 0 and Map[i+1][j-1] == "#":
                count += 1
                visited.append((i+1, j-1))
            if i < n-1 and j < m-1 and Map[i+1][j+1] == "#":
                count += 1
                visited.append((i+1, j+1))
            if i > 0 and j > 0 and Map[i-1][j-1] == "#":
                count += 1
                visited.append((i-1, j-1))
            if count == int(now):
                for y, x in visited:
                    r[y][x] = "P"
        if r[i][j] != "P":
            r[i][j] = now
r = ["".join(row) for row in r]
sys.stdout.write("\n".join(r))
        
