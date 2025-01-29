n,m,d = map(int, input().split())
if n > m:
    n,m = m,n
if n > d:
    print("NO")
else:
    r = "NO"
    for i in range(d//m+1):
        if (d-m*i) % n == 0:
            r = "YES"
            break
    print(r)
