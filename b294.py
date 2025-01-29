n = int(input())
nums = list(map(int, input().split()))
r = 0
for i in range(1,1+n):
    r += nums[i-1]*i
print(r)
