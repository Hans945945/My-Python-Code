m,n,k = map(int, input().split())
a =[list(input()) for _ in range(m)]
moves = input().split()
y,x = m-1, 0
r = []
for t in moves:
    if t == "0":
        y-=(y!=0)
    elif t == "1":
        x+=(x!=n-1)
    elif t == "2":
        if y != m-1 and x != n-1:
            y+=1
            x+=1
    elif t == "3":
        y+=(y!=m-1)
    elif t == "4":
        x-=(x!=0)
    else:
        if x != 0 and y != 0:
            x-=1
            y-=1
    r.append(a[y][x])
print("".join(r))
print(len(set(r)))
