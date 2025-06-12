n,m,k = map(int, input().split())
boss = []
for _ in range(k):
    r,c,s,t = map(int, input().split())
    boss.append([r,c,s,t,1])
bombs = set()
alive = k
while alive > 0:
    for i in range(k):
        if boss[i][4] == 0:
            continue
        r,c,s,t = boss[i][0],boss[i][1],boss[i][2],boss[i][3]
        bombs.add((r,c))
        r += s
        if r > n-1 or r<0:
            boss[i][4] = 0
            alive -= 1
            continue
        c += t
        if c > m-1 or c<0:
            boss[i][4] = 0
            alive -= 1
            continue
        boss[i][0] = r
        boss[i][1] = c
    temp = set()
    for i in range(k):
        if boss[i][4]:
            r,c = boss[i][0],boss[i][1]
            if (r,c) in bombs:
                boss[i][4] = 0
                temp.add((r,c))
                alive -= 1
    bombs -= temp
print(len(bombs))
        
        
            
