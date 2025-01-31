import sys
from collections import Counter
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
count_nums = Counter(nums)
sort_nums = sorted(count_nums.items(), key=lambda x: (-x[1], x[0]))
max_n = sort_nums[0][1]
r = []
for key, n in sort_nums:
    if n < max_n:
        break
    r.append(f"{key} {n}")
sys.stdout.write("\n".join(r)+"\n")


