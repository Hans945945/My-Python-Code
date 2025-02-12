import sys
data = sys.stdin.readlines()
n,m = map(int, data[0].split())
need = m*3//2
ranking = []
for s in data[1:]:
    k,s = map(int, s.split())
    ranking.append((k,s))
ranking.sort(key=lambda  x: (-x[1], x[0]))
r = []
goal = ranking[need-1][1]
count = 0
for k,s in ranking:
    if s < goal:
        break
    count += 1
    r.append(f"{k} {s}")
r.insert(0,f"{goal} {count}")
sys.stdout.write("\n".join(r)+"\n")
