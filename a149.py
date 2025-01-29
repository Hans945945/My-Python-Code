T = int(input())
for _ in range(T):
    n = list(map(int, list(input())))
    r = 1
    for i in range(len(n)):
        r *= n[i]
    print(r)
