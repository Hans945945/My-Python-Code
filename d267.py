import sys
from collections import Counter
T = int(input())
for _ in range(T):
    count = Counter([w.lower() for w in sys.stdin.readline().strip() if w.isalpha()])
    max_count = max(count.values())
    print("".join(sorted([l for l, c in count.items() if c == max_count])))
        
