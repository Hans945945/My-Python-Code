M = int(input())
N = 1
l = 1+(M-1)*2
for i in range(M):
    for _ in range((l-N)//2):
        print("_",end = "")
    for _ in range(N):
        print("*", end="")
    for _ in range((l-N)//2):
        print("_",end = "")
    N += 2
    print("\n")
    
    
    
