import re
import sys
data = sys.stdin.readlines()
n1,n2,w = data[0].split()
r = []
for s in data[1:]:
    nums = map(int, re.findall(r'\d+', s.strip()))
    count = 0
    for n in nums:
        if n%int(n1) == 0 or n%int(n2) == 0 or n1 in str(n) or n2 in str(n):
            count += 1
    if count:
        r.append(w*count)
sys.stdout.write("\n".join(r)+"\n")
