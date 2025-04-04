import sys

data = sys.stdin.read().split()
t = int(data[0])
r = []
idx = 1

for _ in range(t):
    n, m = int(data[idx]), int(data[idx + 1])
    idx += 2
    count = 0

    while n >= m:
        count += n // m
        n = n // m + n % m

    r.append(str(count) if n == 1 else "cannot do this")

sys.stdout.write("\n".join(r) + "\n")
