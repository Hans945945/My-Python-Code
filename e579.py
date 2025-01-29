T = int(input())
for _ in range(T):
    N = int(input())
    P = int(input())
    p = []
    b = 0
    for _ in range(P):
        p.append(int(input()))
    p.sort()
    for i in range(N):
        if not (i %7 ==5 or i % 7 == 6):
            for j in range(P):
                if (i+1) % p[j] ==0:
                    b += 1
                    break
    print(b)
                    
