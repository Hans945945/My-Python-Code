M = int(input())
N = 1
for i in range(M):
    for j in range(M):
        if j > M-N-1:
            print("*",end='')
        else:
            print("_",end = "")
    print()
    N = N+1
