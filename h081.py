n,D = map(int, input().split())
stocks = list(map(int, input().split()))
x = stocks[0]
earn = 0
has = True
for y in stocks:
    if y >= x + D and has:
        earn += y-x
        has = False
        x = y
    if not has and y <= x-D:
        has = 1
        x = y
print(earn)
