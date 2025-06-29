T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    print((max(nums)-min(nums))*2)
