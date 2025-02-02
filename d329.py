import sys
data = sys.stdin.read().splitlines()[1:]
for s in data:
    a,b = s.split()
    sys.stdout.write(str(int(str(int(a[::-1]) + int(b[::-1]))[::-1]))+"\n")
