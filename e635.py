while True:
    s = int(input())
    if s == 0:
        break
    n =((8*s+1)**0.5 + 1) // 2
    f = n*(n+1)//2 -s
    print(int(f), int(n))
    
