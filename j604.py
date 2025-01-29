while True:
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        break
    n = temp[0]
    k = temp[1]
    wins = [0]*(n+1)
    loses = [0]*(n+1)
    for _ in range(k*n*(n-1)//2):
        p1, m1, p2, m2 = input().split()
        if m1 == "rock":
            if m2 == "scissors":
                wins[int(p1)] += 1
                loses[int(p2)] += 1
            elif m2 == "paper":
                wins[int(p2)] += 1
                loses[int(p1)] += 1
        elif m1 == "paper":
            if m2 == "rock":
                wins[int(p1)] += 1
                loses[int(p2)] += 1
            elif m2 == "scissors":
                wins[int(p2)] += 1
                loses[int(p1)] += 1
        elif m1 == "scissors":
            if m2 == "paper":
                wins[int(p1)] += 1
                loses[int(p2)] += 1
            elif m2 == "rock":
                wins[int(p2)] += 1
                loses[int(p1)] += 1
    for i in range(1,n+1):
        if wins[i] + loses[i] == 0:
            print("-")
        else:
            print(f"{wins[i] / (wins[i] + loses[i]):.3f}")
    print()
        
