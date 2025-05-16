T = int(input())
for _ in range(T):
    n = int(input())
    left = 0
    right = 2 * 10**9
    while left <= right:
        m = (left+right) // 2
        total = m * (m + 1) // 2
        if total <= n:
            left = m + 1
        else:
            right = m - 1
    print(right)
