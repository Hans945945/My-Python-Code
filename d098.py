import sys
for s in sys.stdin:
    print(sum(map(int, [w for w in s.split() if w.isdigit()])))
