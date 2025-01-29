import sys
for s in sys.stdin:
    print(sum(map(int, s.split()))*2)
