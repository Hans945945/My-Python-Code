import sys
r = []
money = 0
for s in sys.stdin.readlines()[1:]:
    data = s.split()
    if data[0] == "report":
        r.append(money)
    else:
        money += int(data[1])
sys.stdout.write("\n".join(map(str, r))+"\n")
