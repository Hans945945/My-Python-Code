N = int(input())
nums = []
for _ in range(N):
    p,h = map(int, input().split())
    nums.append((p,h))
nums.sort()
last_p,last_h = nums.pop(0)
ans = -1
for p,h in nums:
    if last_h ** 2 - (p - last_p)**2 < (h/2)**2:
        ans = p
        break
    last_p, last_h = p,h
print(ans)
