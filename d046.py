n = int(input())
nums = list(map(int, input().split()))
c = 0
for i in range(n):
    if nums[i] <= 10:
        c += 1
print(c)
