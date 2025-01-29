T = int(input())
for i in range(1,T+1):
    players = list(map(int, input().split()))
    N = players.pop(0)
    print(f"Case {i}: {players[(N+1)//2-1]}")
    
