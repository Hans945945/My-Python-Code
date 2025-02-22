import sys
from collections import defaultdict
def BFS(y,x,l):
    visited[y][x] = 1
    q = [(y,x)]
    while q:
        y,x = q.pop(0)
        if y > 0 and MAP[y-1][x] == l and not visited[y-1][x]:
            visited[y-1][x] = 1
            q.append((y-1,x))
        if y < h-1 and MAP[y+1][x] == l and not visited[y+1][x]:
            visited[y+1][x] = 1
            q.append((y+1,x))
        if x > 0 and MAP[y][x-1] == l and not visited[y][x-1]:
            visited[y][x-1] = 1
            q.append((y,x-1))
        if x < w-1 and MAP[y][x+1] == l and not visited[y][x+1]:
            visited[y][x+1] = 1
            q.append((y,x+1))
    return
data = sys.stdin.readlines()[1:]
idx = 0
r = []
case = 0
while idx < len(data):
    case += 1
    h,w = map(int, data[idx].split())
    idx += 1
    MAP = [list(s.strip()) for s in data[idx:idx + h]]
    idx += h
    visited = [[0]*w for _ in range(h)]
    languages = defaultdict(int)
    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                now = MAP[i][j]
                languages[now] +=1
                BFS(i,j,now)
    r.append(f"World #{case}")
    for l,c in sorted(languages.items(), key = lambda x: (-x[1],x[0])):
        r.append(f"{l}: {c}")
sys.stdout.write("\n".join(r)+"\n")
    
