n = int(input())
if n > 2:
    dp = [0]*(n+1)
    dp[0] = dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[-1])
elif n == 0 or n == 1:
    print(1)
else:
    print(2)
