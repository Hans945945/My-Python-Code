from itertools import accumulate
while True:
    try:
        n,m = map(int, input().split())
        h = list(map(int, input().split()))
        acc = list(accumulate(h))
        for _ in range(m):
            l,r = map(int, input().split())
            r-=1
            l-=1
            if l == 0:
                print(acc[r])
            else:
                print(acc[r]-acc[l-1])
    except EOFError:
        break
