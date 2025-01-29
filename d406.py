case = 1
while True:
    try:
        S = int(input())
        n,m = map(int, input().split())
        tubes = [[] for _ in range(n)]
        for i in range(n):
            tubes[i] = list(map(int, input().split()))
        water = [[0 for _ in range(m)] for _ in range(n)]
        Q = [[tubes[0].index(1),0]]
        water[0][Q[0][0]] = 1
        while len(Q) > 0:
            x,y = map(int, Q.pop(0))
            if x > 0:
                if tubes[y][x-1] == 1 and water[y][x-1] == 0:
                    water[y][x-1] = water[y][x] + 1
                    Q.append([x-1, y])
            if x < m-1:
                if tubes[y][x+1] == 1 and water[y][x+1] == 0:
                    water[y][x+1] = water[y][x] + 1
                    Q.append([x+1, y])
            if y > 0 and S == 1:
                if tubes[y-1][x] == 1 and water[y-1][x] == 0:
                    water[y-1][x] = water[y][x] + 1
                    Q.append([x,y-1])
            if y < n-1:
                if tubes[y+1][x] == 1 and water[y+1][x] == 0:
                    water[y+1][x] = water[y][x] + 1
                    Q.append([x, y+1])
        
        print(f"Case {case}:")
        for i in range(n):
            print(" ".join(map(str, water[i])))
        case += 1
    except EOFError:
        break
