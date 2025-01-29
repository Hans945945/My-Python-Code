N =int(input())
nums = [1,3]
for i in range(2, N):
    nums.append(nums[i-2] + nums[i-1])
print(nums.pop())
