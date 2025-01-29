while True:
    a,b = sorted(map(int, input().split()))
    if a == -1 and b == -1:
        break
    print(min(b-a, 100-b+a))
