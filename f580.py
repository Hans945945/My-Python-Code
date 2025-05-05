n,m = map(int, input().split())
dice = [[1,3,5] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    if a > 0 and b > 0:
        dice[a-1],dice[b-1] = dice[b-1],dice[a-1]
    elif b == -1:
        dice[a-1][0], dice[a-1][1] = dice[a-1][1], 7-dice[a-1][0]
    else:
        dice[a-1][0], dice[a-1][2] = dice[a-1][2], 7-dice[a-1][0]

for i in range(n):
    print(dice[i][0], end = " ")
