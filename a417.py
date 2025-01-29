T = int(input())
for _ in range(T):
    N, m = map(int, input().split())
    Map = [[0 for _ in range(N)] for _ in range(N)]
    delta_x = (m==1)*1
    delta_y = (m==2)*1
    x,y = 0,0
    for i in range(1, N*N+1):
        Map[y][x] = i
        if m == 1:
            if (delta_x == 1 and delta_y == 0) and (x == N-1 or Map[y][x+1] != 0):
                delta_x = 0
                delta_y = 1
            elif (delta_x == 0 and delta_y == 1) and (y == N-1 or Map[y+1][x] != 0):
                delta_x = -1
                delta_y = 0
            elif (delta_x == -1 and delta_y == 0) and (x == 0 or Map[y][x-1] != 0):
                delta_x = 0
                delta_y = -1
            elif (delta_x == 0 and delta_y == -1) and (y == 0 or Map[y-1][x] != 0):
                delta_x = 1
                delta_y = 0
        else:
            if (delta_x == 0 and delta_y == 1) and (y == N-1 or Map[y+1][x] != 0):
                delta_x = 1
                delta_y = 0 
            elif (delta_x == 1 and delta_y == 0) and (x == N-1 or Map[y][x+1] != 0):
                delta_x = 0
                delta_y = -1
            elif (delta_x == 0 and delta_y == -1) and (y == 0 or Map[y-1][x] != 0):
                delta_x = -1
                delta_y = 0
            elif (delta_x == -1 and delta_y == 0) and (x == 0 or Map[y][x-1] != 0):
                delta_x = 0
                delta_y = 1
             
        x += delta_x
        y += delta_y
    Map = ["".join([f"{j: 5d}" for j in i]) for i in Map]
    print("\n".join(Map))
