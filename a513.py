import heapq

T = int(input())
r = []

for i in range(T):
    N,M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums_heap = [-n for n in nums]
    heapq.heapify(nums_heap)
    
    print(f"Case {i+1}:")
    for _ in range(M):
        status = list(map(int, input().split()))
        if status[0] == 1:
            heapq.heappush(nums_heap,-status[1])
        else:
            if nums_heap:
                value = -heapq.heappop(nums_heap)
                print("Max:", value)
            else:
                print("It's empty!")
    if nums_heap:
        print(" ".join(map(str, sorted([-n for n in nums_heap], reverse = True))))
    else:
        print("It's empty!")
        
        
