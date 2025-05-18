import sys
data = sys.stdin.readlines()
n = int(data[0])
temp = list(map(int, data[1].split()))
a = [0]*n
for i in range(n):
    a[temp[i]-1] = i+1
MAP = {v: i for i, v in enumerate(a)}
for s in data[2:]:
    temp = list(map(int, s.split()))
    nums = [0]*n
    for i in range(n):
        nums[temp[i]-1] = i+1
    nums = [MAP[i] for i in nums]
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))

    
