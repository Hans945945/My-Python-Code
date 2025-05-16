from bisect import bisect_left as left
m, n = map(int, input().split())
nums = list(map(int, input().split()))
xs = list(map(int, input().split()))
total = 0

for x in xs:
    idx = left(nums, x)
    total += (idx+1) * 2

print(total)
