n,m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
input()
temp = [list(map(int, input().split())) for _ in range(n)]
rows = [sum(temp[i]) for i in range(n)]
cols = [sum(t) for t in list(zip(*temp))]
for i in range(n):
    for j in range(m):
        if (rows[i] + cols[j] - temp[i][j]) % 2 == 1:
            MAP[i][j] = 0 if MAP[i][j] == 1 else 1
        print(MAP[i][j], end = " ")
    print()

