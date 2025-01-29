x = 1
while True:
    try:
        n,m = map(int, input().split())
        table = []
        for _ in range(n):
            temp = list(map(int, input().split()))
            table.append(temp)
        for i in range(n):
            for j in range(m):
                if i != 0 and j != 0:
                    table[i][j] += min(table[i-1][j], table[i][j-1])
                elif i != 0:
                    table[i][j] += table[i-1][j]
                elif j != 0:
                    table[i][j] += table[i][j-1]
        print(f"Case #{x} :")
        print(table[n-1][m-1])
        x+=1
    except EOFError:
        break
