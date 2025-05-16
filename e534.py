import sys

s = sys.stdin.read().splitlines()
for i in range(0, len(s), 6):
    seen = {}
    count = 0
    for j in range(6):
        w, h = map(int, s[i+j].split())
        temp = tuple(sorted((w, h)))
        if temp not in seen:
            seen[temp] = 1
        else:
            seen[temp] += 1

    if len(seen) == 3 and all(v == 2 for v in seen.values()):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
