r,a = map(int, input().split())
if r == a:
    o = [a-3,3]
else:
    o = [a,r-a]
o.sort()
print(f"{o[0]}+{o[1]}={r}")
