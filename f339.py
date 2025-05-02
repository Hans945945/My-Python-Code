import sys

data = sys.stdin.readlines()
n, m = map(int, data.pop(0).split())
segments = []

for i in range(m):
    s, e = map(int, data[i].split())
    segments.append((s, e))

segments.sort()

merged = []
for s, e in segments:
    if s == e:
        continue
    if not merged or s > merged[-1][1]:
        merged.append((s, e))
    else:
        last_s, last_e = merged[-1]
        merged[-1] = (last_s, max(last_e, e))

r = []
last = 0
for s, e in merged:
    if last < s:
        r.append(f"{last} {s}")
    last = max(last, e)

if last < n:
    r.append(f"{last} {n}")

sys.stdout.write("\n".join(r) + "\n")
