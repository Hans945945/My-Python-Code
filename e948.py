N = int(input())
for _ in range(N):
    G, A, H, W = map(int, input().split())
    if G:
        r = 13.7*W + 5*H - 6.8*A + 66
    else:
        r = 9.6*W + 1.8*H - 4.7*A + 655
    print(f"{r:.2f}")
