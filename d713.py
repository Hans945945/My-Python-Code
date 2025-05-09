import heapq
import sys

low = [] 
high = []

for s in sys.stdin:
    num = int(s)
    heapq.heappush(low, -num)
    heapq.heappush(high, -heapq.heappop(low))
    if len(high) > len(low):
        heapq.heappush(low, -heapq.heappop(high))
    if len(low) > len(high):
        print(-low[0])
    else:
        print((-low[0] + high[0]) // 2)
