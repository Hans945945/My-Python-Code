import sys
for s in sys.stdin.readlines():
    n = int(s)
    print(1 + (n - 1) % 9 if n else 0)
