n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
r = []
for i in range(n):
    for j in range(m):
        total = 0
        x = nums[i][j]
        for k in range(i-x, i+x+1):
            for l in range(j-(x-abs(k-i)), j + (x-abs(k-i) + 1)):
                if 0 <= k < n and 0 <= l < m:
                    total += nums[k][l]
                    
        if total % 10 == x:
            r.append(f"{i} {j}")
print(len(r))
print('\n'.join(r))
