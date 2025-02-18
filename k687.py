import sys
scores = []
case = 0
for s in sys.stdin.readlines()[1:]:
    case += 1
    temp = s.strip()
    for i in range(len(temp)):
        if temp[i].isdigit():
            player = temp[:i]
            score = int(temp[i:])
            scores.append((score, -case, player))
            break
scores.sort(reverse = True)
rank = 0
last = float('inf')
r = []
for s,_,p in scores:
    if s < last:
        rank += 1
    r.append(f"{rank} {p} {s}")
    last = s
sys.stdout.write("\n".join(r)+"\n")
