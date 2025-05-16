import sys
for s in sys.stdin:
    n = int(s)
    print((n//2+1) * (n//2+2) // 2)
