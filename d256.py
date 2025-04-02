import sys

def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

data = sys.stdin.readlines()
T = int(data.pop(0))
r = []

for i in range(T):
    G, L = map(int, data[i].split())

    if L % G != 0:
        r.append("-1")
        continue

    k = L // G
    min_x, min_y = None, None

    for x in range(1, int(k**0.5) + 1):
        if k % x == 0:
            y = k // x
            if GCD(x, y) == 1:
                min_x, min_y = x, y
                break

    if min_x is not None:
        r.append(f"{G * min_x} {G * min_y}")
    else:
        r.append("-1")

sys.stdout.write("\n".join(r) + "\n")
