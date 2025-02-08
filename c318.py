import sys
n,t = map(int, sys.stdin.readline().split())
score = []
ds = []
for s in sys.stdin:
    s,d = map(int, s.split())
    score.append(s)
    ds.append(d)
total = 0
for _ in range(t):
    now = max(score)
    if now == 0:
        break
    total += now
    idx = score.index(now)
    score[idx] -= ds[idx]
    if score[idx] < 0:
        score[idx] = 0
print(total)
