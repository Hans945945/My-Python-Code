while True:
    try:
        a,b,c,d = map(int, input().split())
        A = []
        B = []
        if b == c:
            for _ in range(a):
                temp = list(map(int, input().split()))
                A.append(temp)
            for _ in range(c):
                temp = list(map(int, input().split()))
                B.append(temp)
            for i in range(a):
                for j in range(d):
                    count = 0
                    for k in range(b):
                        count += A[i][k]*B[k][j]
                    print(count, end = " ")
                print()
        else:
            print("Error")
    except:
        break
