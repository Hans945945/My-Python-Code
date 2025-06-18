n = int(input())
MAP = [list(input()) for _ in range(n)]
r = [["0"]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if MAP[i][j] == "*":
            r[i] = ["*"]*n
            for k in range(n):
                r[k][j] = "*"
print("\n".join("".join(row) for row in r))
