a = input()
b = input()
T = int(input())
n,m = len(a), len(b)
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
print("sitini na tisa" if dp[n][m] < T else "kwa nini unaendesha")
