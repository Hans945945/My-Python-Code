N = int(input())
c = []
for _ in range(N):
    data = input().split()
    data[0] = int(data[0])
    data.insert(0,-1*sum(map(int, data[2:])))
    c.append(data)
c.sort()
rank = 0
rank_now = 0
now = -1
for i in range(N):
    c[i][0] *= -1
    temp = c[i].pop(0)
    c[i].append(temp)
    rank_now +=1
    if temp != now:
        now = temp
        rank = rank_now
    c[i].append(rank)
    print(" ".join(list(map(str, c[i]))))
    
        
    
    
