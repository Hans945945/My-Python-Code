while True:
    n,m = map(int, input().split())
    if n == 0 and m == 0:
        break
    words = ""
    for _ in range(n):
        words+=input()
    index = list(map(int, input().split()))
    r = []
    for i in range(m):
        r.append(words[index[i]-1])
    print("".join(r))
