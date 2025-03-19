import sys
r = []
for s in sys.stdin.readlines()[1:]:
    e,f,c = map(int, s.split())
    count = 0
    e += f
    while e >= c:
        count += e//c
        e = e//c + e%c
    r.append(count)
sys.stdout.write("\n".join(map(str, r))+"\n")
