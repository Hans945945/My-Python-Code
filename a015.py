while True:
    try:
        r,c = map(int, input().split())
        A = []
        for _ in range(r):
            temp = list(map(int, input().split()))
            A.append(temp)
        A = list(zip(*A))
        for i in range(c):
            print(" ".join(map(str, A[i])))

    except EOFError:
        break
