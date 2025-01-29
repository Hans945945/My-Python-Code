n = int(input())
g = list(map(int, input().split()))
found = False
j = 0
if g.count(1) < 2:
    print(0)
else:
    while not found:
        if g[j] == 1:
            g[0:j] = [1 for i in range(j)]
            found = True
        j+=1
    found = False
    j = n-1
    while not found:
        if g[j] == 1:
            g[j:n] = [1 for i in range(n-j)]
            found = True
        j-=1
    for i in range(n):
        if g[i] == 9:
            if g[i+1] != 9:
                if g != 0:
                    g[i-1] = 1
                if g != n:
                    g[i+1] = 1
            else:
                if g != 0:
                    g[i-1] = 1
    print(g.count(0))
