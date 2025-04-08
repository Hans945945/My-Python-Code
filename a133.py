import sys

r = []
data = sys.stdin.readlines()[:-1]
for k in range(0, len(data), 3):
    n, m = map(int, data[k].split())
    a = list(map(int, data[k+1].split()))
    b = list(map(int, data[k+2].split()))

    dp= [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    r.append(f"Twin Towers #{k//3 + 1}")
    r.append(f"Number of Tiles : {dp[n][m]}")
    r.append('')

sys.stdout.write("\n".join(r) + "\n")

            
