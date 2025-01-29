from collections import Counter
import sys
for s in sys.stdin:
    temp = Counter(s.strip())
    print("\n".join(f"{-k} {v}" for v, k in sorted([(value, -ord(key)) for key, value in temp.items()])))
    print()
