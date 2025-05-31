H, W, N = map(int, input().split())
canvas = [[0] * W for _ in range(H)]

for _ in range(N):
    r, c, t, x = map(int, input().split())
    for i in range(H):
        for j in range(W):
            if abs(i-r) + abs(j-c) <= t:
                canvas[i][j] += x

for row in canvas:
    print(" ".join(map(str, row)))

