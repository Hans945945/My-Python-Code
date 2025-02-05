import sys
from collections import defaultdict
sign_in = defaultdict(int)
data = sys.stdin.read().splitlines()
for s in data[:-1]:
    t,i = s.split()
    if t == "0":
        sign_in[i] = 0
    else:
        sign_in[i] += 1
print(sum(sign_in.values()))
