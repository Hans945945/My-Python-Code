data = list(map(int,input().split()))
N = data[0]
M = data[1]
x = data[2]
y = data[3]
f = True
r = [-1,-1]
for i in range(N+1):
    if i*x+(M-i)*y == N and i>=0 and (M-i)>=0:
        r[0] = i
        r[1] = M-i
        break
print(r[0],r[1])
            
