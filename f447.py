import sys
T = int(input())
for s in sys.stdin:
    n,m = map(int, s.split())
    print((m-1+m-n)*n//2)
