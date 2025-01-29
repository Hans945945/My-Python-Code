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
            if j < m-1 and Map[i][j+1] == "P":
                count += 1
            if j > 0 and Map[i][j-1] == "P":
                count += 1
            if i < n-1 and Map[i+1][j] == "P":
                count += 1
            if i > 0 and Map[i-1][j] == "P":
                count += 1
            if i > 0 and j < m-1 and Map[i-1][j+1] == "P":
                count += 1
            if i < n-1 and j > 0 and Map[i+1][j-1] == "P":
                count += 1
            if i < n-1 and j < m-1 and Map[i+1][j+1] == "P":
                count += 1
            if i > 0 and j > 0 and Map[i-1][j-1] == "P":
                count += 1
            if count == int(now):
                if (j < m-1 and Map[i][j+1] == "#") or (j > 0 and Map[i][j-1] == "#") or (i < n-1 and Map[i+1][j] == "#") or (i > 0 and Map[i-1][j] == "#") or (i > 0 and j < m-1 and Map[i-1][j+1] == "#") or (i < n-1 and j > 0 and Map[i+1][j-1] == "#") or (i < n-1 and j < m-1 and Map[i+1][j+1] == "#") or (i > 0 and j > 0 and Map[i-1][j-1] == "#"):
                    r[i][j] = "O"
            else:
                r[i][j] = now
        else:
            r[i][j] = now
r = ["".join(row) for row in r]
sys.stdout.write("\n".join(r))
