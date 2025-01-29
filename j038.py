T = int(input())
for _ in range(T):
    land = []
    while True:
        n = int(input())
        if n == 0:
            break
        land.append(n)
    land.sort(reverse = True)
    price = sum([2*pow(land[i], i+1) for i in range(len(land))])
    print("Too expensive" if price > 5000000 else price)
