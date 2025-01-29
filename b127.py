def F(n):
    if n <= 1:
        used[n-1] = 1
        return 1
    elif used[n-1] != 0:
        return used[n-1]
    else:
        used[n-1] = F(n-1)+ F(n-2)
        return used[n-1]
    
used = [0 for i in range(45)]
F(45)
while True:
    try:
        N = int(input())
        print(used[N-1])
    except:
        break
