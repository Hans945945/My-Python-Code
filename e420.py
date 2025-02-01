import sys
from collections import defaultdict
data = sys.stdin.read().splitlines()
index = 0
total = 1
clothes = defaultdict(int)
same = None
first = 1
while True:
    temp = set()
    now = data[index]
    while now != "@" and now != "#":
        clothes[now] += 1
        temp.add(now)
        index += 1
        now = data[index]
    index += 1
    total *= len(temp)
    if same is None:
        same = temp
    else:
        same &= temp
    if now == "#":
        break
max_n = max(clothes.values())
r = [str(total), ",".join(sorted(key for key,value in clothes.items() if value == max_n)),",".join(sorted(same))]
sys.stdout.write("\n".join(r)+"\n")
