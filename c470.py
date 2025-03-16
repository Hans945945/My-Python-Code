n = int(input())
nums = list(map(int, input().split()))
odd = even = 0
for i in range(len(nums)):
    if i % 2 == 0:
        even += nums[i]
    else:
        odd += nums[i]
print(max(even, odd))
