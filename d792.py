def bfs(s, MAP):
    l = [-1]*n
    q = [s]
    l[s] = 0
    while q:
        u = q.pop(0)
        for v in MAP[u]:
            if l[v] == -1:
                l[v] = l[u]+1
                q.append(v)
    return l

T = int(input())
for case in range(1, T + 1):
    n = int(input())
    MAP = [[] for _ in range(n)]

    r = int(input())
    for _ in range(r):
        u, v = map(int, input().split())
        MAP[u].append(v)
        MAP[v].append(u)
    
    s, d = map(int, input().split())

    s2b = bfs(s, MAP)
    b2d = bfs(d, MAP)

    print(f"Case {case}: {max(s2b[i] + b2d[i] for i in range(n))}")
