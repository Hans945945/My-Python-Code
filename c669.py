import sys
T = int(input())
for s in sys.stdin:
    nums = sorted(map(int, s.split()))
    for n in nums:
        if nums.count(n) == 2:
            a = n
            nums.pop(nums.index(n))
            break
    b = (nums[0] + nums[-1])*(len(nums)+1)//2 - sum(nums)
    print(b,a)
