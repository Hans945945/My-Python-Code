while True:
    try:
        n,m = map(int, input().split())
        cars = []
        for _ in range(n):
            cars.append(input().split())
        for _ in range(m):
            Type, index = input().split()
            if Type == "color":
                for i in range(n):
                    if cars[i][1] == index:
                        print(" ".join(cars[i]))
            else:
                for i in range(n):
                    if cars[i][0] == index:
                        print(" ".join(cars[i]))
        print()
        input()
    except EOFError:
        break
