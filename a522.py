import sys

data = sys.stdin.readlines()
T = int(data.pop(0))
r = []

for i in range(0,T*3,3):
    target = int(data[i])
    bars = list(map(int, data[i+2].split()))

    dp = [0] * (target+1)
    dp[0] = 1

    for bar in bars:
        for i in range(target, bar-1, -1):
            if dp[i - bar]:
                dp[i] = 1

    r.append("YES" if dp[target] else "NO")

print("\n".join(r)+"\n")
