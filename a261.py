import sys
from bisect import bisect_left

dp = [[0] * 64 for _ in range(101)]
for i in range(1, 101):
    for j in range(1, 64):
        dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] + 1

data = sys.stdin.read().split()
res = []

for i in range(0, len(data), 2):
    k = int(data[i])
    if k == 0:
        break
    n = int(data[i + 1])

    if dp[k][63] < n:
        res.append("More than 63 trials needed.")
    else:
        j = bisect_left(dp[k], n)
        res.append(str(j))

sys.stdout.write("\n".join(res) + "\n")
