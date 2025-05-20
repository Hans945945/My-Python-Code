from collections import defaultdict, deque

T = int(input())
MAP = defaultdict(list)
for _ in range(T):
    a, b = input().split()
    MAP[a].append(b)
    MAP[b].append(a)

l, o = input().split()

queue = deque([(l, 0)])
visited = set()
visited.add(l)

not_found = 1
while queue:
    n,d = queue.popleft()
    if n == o:
        print(f"True {d}")
        not_found = 0
        break
    for x in MAP[n]:
        if x not in visited:
            visited.add(x)
            queue.append((x,d+1))

if not_found:
    print("False")
