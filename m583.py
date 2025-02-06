import sys
n = int(sys.stdin.readline())
points = list(map(int, sys.stdin.readline().split()))
visited = [0] * (n + 1)
max_n = 0
for p in range(1, n + 1):
    if not visited[p]:
        count = 0
        now = p
        while not visited[now]:
            visited[now] = 1
            now = points[now - 1]
            count += 1
        max_n = max(max_n, count)

print(max_n)
