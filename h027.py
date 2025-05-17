s,t,n,m,r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(s)]
B = [list(map(int, input().split())) for _ in range(n)]
Min = float("inf")
count = 0
S = sum(sum(a) for a in A)
for i in range(0,n-s+1):
    for j in range(0,m-t+1):
        temp = 0
        total = 0
        for k in range(s):
            for l in range(t):
                total += B[i+k][j+l]
                if A[k][l] != B[i+k][j+l]:
                    temp += 1
        if temp <= r:
            count += 1
            Min = min(Min, abs(total-S))
print(count, Min if Min != float("inf") else -1, sep = "\n")
