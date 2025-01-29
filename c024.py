import sys
for s in sys.stdin:
    n = int(s)
    if n < 0:
        break
    print(1+n*(n+1)//2)
