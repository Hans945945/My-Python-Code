T = int(input())
for _ in range(T):
    n,m = map(int, input().split())
    m1 = []
    m2 = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        m1.append(temp.copy())
        temp.reverse()
        m2.append(temp)
    m2.reverse()
    if m1 == m2:
        print("go forward")
    else:
        print("keep defending")
