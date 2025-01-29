import math
N = int(input())
for i in range(N):
    n = int(input())
    prime = 1
    for j in range(1,round(math.sqrt(n))+1):
        if n%j == 0 and j != 1 and j != n:
            prime = 0
            print("N")
            break
    if prime:
        print("Y")
