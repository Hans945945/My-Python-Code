import sys
from itertools import combinations
r = []
for s in sys.stdin.readlines()[:-1]:
    nums = list(map(int, s.split()))
    n = nums.pop(0)
    m = nums.pop()
    unique = sorted(set(tuple(sorted(comb)) for comb in combinations(nums, m)))
    r.extend(" ".join(map(str, p)) for p in unique)
    r.append("")
sys.stdout.write("\n".join(r)+"\n")
