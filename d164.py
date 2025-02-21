import sys

r = []
data = sys.stdin.readlines()
idx = 0

while idx < len(data):
    n, m = map(int, data[idx].split())
    idx += 1
    cows = list(map(int, data[idx:idx + n]))
    idx += n

    cows.extend(cows[:m-1])

    now = sum(cows[:m])
    max_q = now

    for i in range(1, n):
        now += cows[i + m - 1] - cows[i - 1]
        max_q = max(max_q, now)

    r.append(max_q)

sys.stdout.write("\n".join(map(str, r)) + "\n")
