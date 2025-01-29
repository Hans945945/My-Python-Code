import sys
N = int(input())
for s in sys.stdin:
    sys.stdout.write(" ".join(map(str, sorted(map(int, s.split())))))
