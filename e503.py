import sys
from collections import Counter

r = []
for s in sys.stdin:
    count = Counter(c for c in s.rstrip() if c.isalpha())
    max_v = max(count.values())
    words = sorted([k for k, v in count.items() if v == max_v])
    r.append(f"{''.join(words)} {max_v}")
    
sys.stdout.write("\n".join(r) + "\n")
