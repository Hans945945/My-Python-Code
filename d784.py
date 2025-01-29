from itertools import accumulate
T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    nums.pop(0)
    min_prefix_sum = 0
    max_sum = float("-inf")
    for now in accumulate(nums):
        max_sum = max(max_sum, now - min_prefix_sum)
        min_prefix_sum = min(min_prefix_sum, now)
    print(max_sum)
    
