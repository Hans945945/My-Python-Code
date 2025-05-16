import sys
n = int(input())
d = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

for _ in range(d):
    nums = [list(row) for row in zip(*nums)][::-1]

x = y = n // 2
d = 0  # 0左 1上 2右 3下
i = 0
count = 1
r = [nums[y][x]]

while count < n*n:
    diff = i//2+1
    if count + diff > n*n:
        diff = n * n - count

    if d == 0: 
        for _ in range(diff):
            x -= 1
            r.append(nums[y][x])
    elif d == 1: 
        for _ in range(diff):
            y -= 1
            r.append(nums[y][x])
    elif d == 2: 
        for _ in range(diff):
            x += 1
            r.append(nums[y][x])
    else: 
        for _ in range(diff):
            y += 1
            r.append(nums[y][x])

    count += diff
    i += 1
    d = (d + 1) % 4

print("".join(map(str, r)))
