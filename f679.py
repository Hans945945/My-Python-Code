from bisect import bisect_left
import sys

n, q = map(int, input().split())
nums = input().split()
for i in range(n):
    nums[i] = int(nums[i])
r = []

for i in range(q):
    t = int(input())
    idx = bisect_left(nums,t)
    r.append('Yes' if nums[idx] == t else 'No')
    if len(r) == 100000:
        sys.stdout.write("\n".join(r)+"\n")
        r = []
sys.stdout.write("\n".join(r)+"\n")
