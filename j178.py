from itertools import accumulate
m, level = map(int, input().split())
nums = list(map(int, input().split()))
nums.insert(0, level)
r = list(accumulate(nums))
flag = 1
for i in range(m):
    if r[i] <= nums[i+1]:
        print(r[i])
        flag = 0
        break
if flag:
    print(r[-1])
