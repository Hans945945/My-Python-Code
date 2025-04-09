import sys
r = []

Class = [[] for _ in range(5)]

for line in sys.stdin.readlines()[1:]:
    d, s, t = map(int, line.split())
    Class[d-1].append((t, s))

count = 0
for i in range(5):
    if not Class[i]:
        continue

    Class[i].sort()
    end = 0
    for t, s in Class[i]:
        if s >= end:
            count += 1
            end = t

print(count)
