import heapq
N = int(input())
pairs = []
for _ in range(N):
    a,b = map(int, input().split())
    heapq.heappush(pairs, -max(a,b,0))
total = 0
for k in range(N):
    total -= heapq.heappop(pairs)
    print(total)
