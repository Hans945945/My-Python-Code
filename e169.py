import sys
from collections import Counter
data = sys.stdin.readlines()[:-1]
r = []
for i in range(0,len(data),2):
    nums = list(map(int, data[i+1].split()))
    count = Counter()
    pairs = 0
    for num in nums:
        mod = num % 100
        complement = (100 - mod) % 100
        pairs += count[complement]
        count[mod] += 1

    r.append(pairs)
sys.stdout.write("\n".join(map(str, r))+"\n")
