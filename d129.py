n = 1500
dp = [0]*n
dp[0] = 1
i2 = i3 = i5 = 0
next2 = 2
next3 = 3
next5 = 5
for i in range(1, n):
    next_n = min(next2, next3, next5)
    dp[i] = next_n
    if next_n == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if next_n == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if next_n == next5:
        i5 += 1
        next5 = dp[i5] * 5
print(f"The 1500'th ugly number is {dp[-1]}.")
