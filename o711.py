N = int(input())
w1, w2, h1, h2 = map(int, input().split())
nums = list(map(int, input().split()))

w1*= w1
w2*= w2
level = 0
ans = 0

for n in nums:
    prev = level

    if level < h1:
        cap = (h1 - level) * w1
        use = min(n, cap)
        level += use // w1
        n -= use

    if n > 0 and level < h1 + h2:
        cap = (h1 + h2 - level) * w2
        use = min(n, cap)
        level += use // w2

    ans = max(ans, level - prev)

print(ans)
