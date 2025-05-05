n = int(input())
nums = list(map(int, input().split()))
x = min(nums)
smallest = [i for i in range(n) if nums[i] == x]
if len(smallest) == 1:
    print(nums[nums[smallest[0]+x]-1])
else:
    print(nums[nums[smallest[-1]-x]-1])
