import sys
from collections import defaultdict
idx = 0
data = sys.stdin.readlines()
r = []
while idx < len(data):
    n,m = map(int, data[idx].split())
    idx += 1
    nums = list(map(int, data[idx].split()))
    count = defaultdict(int)
    index = {}
    for i in range(n):
        N = nums[i]
        count[N] += 1
        index[f"{count[N]} {N}"] = i+1
    for _ in range(m):
        idx += 1
        r.append(index.get(data[idx].strip(),0))
    idx += 1
sys.stdout.write("\n".join(map(str, r))+"\n")
        
        
