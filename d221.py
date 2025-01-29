import heapq
n = int(input())
while n != 0:
    nums = list(map(int, input().split()))
    cost = 0
    heapq.heapify(nums)
    while len(nums) > 1:
        smallest = heapq.heappop(nums)
        second_smallest = heapq.heappop(nums)
        merge_cost = smallest + second_smallest
        cost += merge_cost
        heapq.heappush(nums, merge_cost)
    print(cost)
    n = int(input())
