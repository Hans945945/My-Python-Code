import sys
s,m,l = map(int, sys.stdin.readline().split())
old = s+m+l
n = int(sys.stdin.readline())
cars = list(map(int, sys.stdin.readline().split()))
cars.sort(reverse = True)
for c in cars:
    if c >= 500:
        if l > 0:
            l -= 1
    elif c >=200:
        if l>0:
            l-=1
        elif m > 0:
            m-=1
    else:
        if l>0:
            l-=1
        elif m>0:
            m-=1
        elif s > 0:
            s -= 1
print(old-s-m-l)
