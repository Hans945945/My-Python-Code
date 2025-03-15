import sys
r = []
for s in sys.stdin:
    n = s.strip()[::-1]
    total = 0
    for i in range(len(n)):
        if n[i] == "1":
            if i %2 == 0:
                total += 2**i
            else:
                total -= 2**i
    r.append(total)
sys.stdout.write("\n".join(map(str, r))+"\n")
