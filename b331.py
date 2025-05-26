a = input().split("+")
ans = 0
for b in a:
    if "*" in b:
        d = 1
        for c in b.split("*"):
            d*=int(c)
        ans += d
    else:
        ans += int(b)
print(str(ans)[-4:] if ans > 9999 else ans)
