import sys

for s in sys.stdin:
    s = s.rstrip()
    new = s[::-1]+ '#' + s
    dp = [0] * len(new)

    for i in range(1, len(new)):
        j = dp[i - 1]
        while j > 0 and new[i] != new[j]:
            j = dp[j - 1]
        dp[i] = j + (new[i] == new[j])

    print(s + s[:len(s) - dp[-1]][::-1])
