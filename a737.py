import sys
for s in sys.stdin.readlines()[1:]:
    nums = list(map(int, s.split()))[1:]
    nums.sort()
    m = nums[len(nums)//2]
    print(sum(abs(n-m) for n in nums))
