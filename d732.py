n,k = map(int, input().split())
a = list(map(int, input().split()))
k = list(map(int, input().split()))
for i in k:
    l,r = 0, len(a)-1
    while l <= r:
        m = (l+r)//2
        if i == a[m]:
            print(m+1)
            break
        elif i < a[m]:
            r = m-1
        else:
            l = m+1
    else:
        print(0)
        
