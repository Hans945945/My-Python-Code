n, m, k = map(int, input().split())
Q = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    Q[i] = temp
price = [0]*k

for s in range(k):
    c = list(map(int, input().split()))

    flow = [[0 for _ in range(m)] for _ in range(m)]

    for x in range(n):
        for y in range(m):
            flow[c[x]][y]+=Q[x][y]

    for u in range(m):
        for v in range(m):
            f = flow[u][v]
            if u == v:
                price[s] += f
            else:
                if f <= 1000:
                    price[s] += f*3
                else:
                    price[s] += 3000+2*(f-1000)

print(min(price))
