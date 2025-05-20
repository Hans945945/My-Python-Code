import sys
from collections import deque, defaultdict

data = sys.stdin.readlines()
N, M, L, Q = map(int, data[0].split())

MAP = defaultdict(list)
for i in range(M):
    a, b = map(int, data[1+i].split())
    MAP[a].append(b)

bad = [0] * (N + 1)
queue = deque()

for i in range(L):
    x = int(data[1+M+i])
    if not bad[x]:
        bad[x] = 1
        queue.append(x)
        
while queue:
    now = queue.popleft()
    for x in MAP[now]:
        if bad[x] == 0:
            bad[x] = 1
            queue.append(x)

for i in range(Q):
    y = int(data[1+M+L+i])
    print("TUIHUOOOOOO" if bad[y] else "YA~~")
