n = int(input())
nums = []
nums.append(n)
while n != -1:
    n = int(input())
    nums.append(n)
nums.sort(reverse = True)
i = int(input())
print(nums[i-1])
