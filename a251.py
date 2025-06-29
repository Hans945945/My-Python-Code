T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    n = nums.pop(0)
    nums.extend([0]*(n-4))
    for i in range(4,n):
        nums[i] = nums[i-4] + nums[i-1]
    nums.sort()
    print(nums[n//2])
