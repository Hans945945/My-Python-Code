import sys
data = sys.stdin.readlines()
idx = 0
while idx < len(data):
    r = []
    n = int(data[idx])
    if n == 0:
        break
    for _ in range(n):
        idx += 1
        a,b = map(int, data[idx].split())
        S = a+b
        if a > b:
            r.append(((S,3), f">{S}"))
        elif a == b:
            r.append(((S,2), f"={S}"))
        else:
            r.append(((S,1), f"<{S}"))
    idx += 1
    r.sort(reverse = True)
    sys.stdout.write(" ".join(e for _, e in r)+"\n")
