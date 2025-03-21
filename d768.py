#bfs
from collections import deque
def bfs(start):
    Q = deque([i])
    color[i] == 0
    while len(Q) > 0:
        now = Q.popleft()
        for next_node in MAP[now]:
            if color[next_node] == -1:
                visited[next_node] = 1
                color[next_node] = 1-color[now]
                Q.append(next_node)
            elif color[next_node] == color[now]:
                return False
    return True
while True:
    n = int(input())
    if n == 0:
        break
    MAP = [[] for _ in range(n)]
    m = int(input())
    for _ in range(m):
        a,b = map(int, input().split())
        MAP[a].append(b)
        MAP[b].append(a)
        
    visited = [0]*n
    color = [-1]*n
    
    BC = True
    for i in range(n):
        if not visited[i] and color[i] == -1:
            if not bfs(i):
                BC = False
                break
#dfs
'''
def dfs(now, c):
    color[now] = c
    
    for v in MAP[now]:
        if color[v] == -1:
            if dfs(v, 1-color[now]) == False:
                return False
        elif color[v] == color[now]:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    MAP = [[] for _ in range(n)]
    m = int(input())
    for _ in range(m):
        a,b = map(int, input().split())
        MAP[a].append(b)
        MAP[b].append(a)
        
    color = [-1]*n
 
    print("BICOLORABLE." if dfs(0, 0) else "NOT BICOLORABLE.")
    print("BICOLORABLE." if BC else "NOT BICOLORABLE.")
'''
    
