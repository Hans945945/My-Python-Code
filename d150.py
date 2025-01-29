t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    p.sort(reverse = True)
    total = 0
    if n < 3:
        print(0)
    else:
        for i in range(2,n,3):
            total += p[i]
        print(total)
