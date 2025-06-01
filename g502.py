nums =  input().split("+")
ans = 0
for t in nums:
    temp = list(map(int, t.split("*")))
    now = 1
    for t in temp:
        now *= t
    ans += now
print(int(str(ans)[-5:]))
