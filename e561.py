n = int(input())
for _ in range(n):
    L = int(input())
    trains = list(map(int, input().split()))
    S = 0
    for i in range(L):
        for j in range(L-i-1):
            if trains[j] > trains[j+1]:
                temp = trains[j]
                trains[j] = trains[j+1]
                trains[j+1] = temp
                S += 1
    print(f"Optimal train swapping takes {S} swaps.")
    
