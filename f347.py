import sys
import heapq

turtles = []
for s in sys.stdin:
    w, s = map(int, s.split())
    turtles.append((w, s))

turtles.sort(key=lambda x: x[1])

total = 0
heap = []

for w, s in turtles:
    heapq.heappush(heap, -w)
    total += w

    if total > s:
        total += heapq.heappop(heap) #-= -heapq

print(len(heap))
