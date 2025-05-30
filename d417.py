import sys
for s in sys.stdin.readlines():
    k = int(s)
    r = []
    for i in range(k+1, 2*k + 1):
        if (k*i) % (i - k) == 0:
            y = (k*i) // (i - k)
            r.append((y, i))
    print(len(r))
    for x, y in r:
        print(f"1/{k} = 1/{x} + 1/{y}")
