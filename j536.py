n,a = map(int, input().split())
rocks = list(map(int, input().split()))
if a < n:
    biggest = rocks.index(max(rocks))
    left = a//2
    right = a//2
    if biggest < left:
        right += left - biggest
        left = biggest - 0
    elif right+biggest > n-1:
        left += right+biggest-n+1
        right = n-1-biggest
    r1 = sum(rocks[biggest-left:right+biggest+1])
    r2 = sum(rocks) - r1
else:
    r1 = sum(rocks)
    r2 = 0
print(r1, r2)
