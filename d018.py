import sys
r = []
for s in sys.stdin.readlines():
    odd = 0
    even = 0
    for t in s.split():
        i,n = map(float, t.split(":"))
        if i % 2 == 0:
            even += n
        else:
            odd += n
    r.append(f"{odd-even:g}")
sys.stdout.write("\n".join(r)+"\n")
