import sys
count = {}
for s in sys.stdin.readlines():
    if s.rstrip() == "-1":
        continue
    S,N = map(int, s.split())
    count[S] = count.get(S,0) + N
for k,v in sorted(count.items()):
    print(f"{k} {v}")
