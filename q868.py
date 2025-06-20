from collections import deque,defaultdict
n = int(input())

MAP = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    MAP[a].append(b)

f, g = map(int, input().split())

q = deque()
visited = {f}
q.append(f)
flag = 1

while q:
    u = q.popleft()
    if u == g:
        print("Yay")
        flag = 0
        break

    if u in MAP:
        for v in MAP[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)

if flag:
    print("Come on")
