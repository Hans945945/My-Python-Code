import sys
from itertools import combinations
r = []
for s in sys.stdin.readlines()[:-1]:
    n,m = map(int, s.split())
    n = ''.join(chr(97+i) for i in range(n))
    r.extend([''.join(nums) for nums in combinations(n,m)])
sys.stdout.write("\n".join(r)+"\n")
