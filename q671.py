def capable(W):
    count = 1
    now = 0
    for w in ws:
        if w > W:
            return 0
        if now + w > W:
            count += 1
            now = w
        else:
            now += w
    return count <= t
n,t,l,r = map(int, input().split())
ws = list(map(int, input().split()))
ans = -1
while l <= r:
    m = (l+r)//2
    if capable(m):
        ans = m
        r = m-1
    else:
        l = m+1
print(ans)
