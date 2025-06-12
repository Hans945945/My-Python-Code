n,e = map(int, input().split())
MAP = [[] for _ in range(n+1)]

ways = [0] * n
for _ in range(e):
    u,v = map(int, input().split())
    MAP[u].append(v)
    ways[v] += 1

q = []
for i in range(n):
    if ways[i] == 0:
        q.append(i)

path = []
while q:
    u = q.pop(0)
    path.append(u)
    for v in MAP[u]:
        ways[v] -= 1
        if ways[v] == 0:
            q.append(v)
            
dp = [0]*(n+1)
dp[0] = 1
for u in path:
    for v in MAP[u]:
        dp[v] += dp[u]

print(dp[n-1])
