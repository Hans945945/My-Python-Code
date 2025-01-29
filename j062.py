case = 1
while True:
    n = int(input())
    if n == 0:
        break
    square = []
    for _ in range(n):
        square.append(list(map(int, input().split())))
    r = []
    for i in range(n,0,-2):
        now = 0
        for j in range((n-i)//2, (n-i)//2+i):
            now += sum(square[j][(n-i)//2:(n-i)//2+i])
        r.append(now)
    for i in range(n//2-(n%2 == 0)):
        r[i] -= r[i+1]
    print(f'Case {case}: {" ".join(map(str, r))}')
    case += 1
