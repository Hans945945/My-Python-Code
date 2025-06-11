n, m = map(int, input().split())
nums = [list(map(int, input().split())) + [1001] for _ in range(n)]
nums.append([1001] * (m + 1))

ans = 0
flag = 1

while flag:
    flag = 0
    for r in range(n):
        for c in range(m):
            if nums[r][c] < 0:
                continue

            i = r + 1
            while nums[i][c] < 0:
                i += 1
            if nums[r][c] == nums[i][c]:
                ans += nums[r][c]
                nums[r][c] = nums[i][c] = -1
                flag = 1
                continue

            j = c + 1
            while nums[r][j] < 0:
                j += 1
            if nums[r][c] == nums[r][j]:
                ans += nums[r][c]
                nums[r][c] = nums[r][j] = -1
                flag = 1

print(ans)
