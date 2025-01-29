T = int(input())
for _ in range(T):
    n = int(input())
    c = list(map(int, input().split()))
    m = 0
    count = 0
    for i in range(n):
        if m < c[i]:
            m = m+c[i]
            count += 1
        else:
            m-=c[i-1]
            m+=c[i]
    print(count)
