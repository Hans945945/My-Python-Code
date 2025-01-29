n = int(input())
for _ in range(n):
    f = int(input())
    money = 0
    for _ in range(f):
        area, animal, r = map(int, input().split())
        money += area*r
    print(money)
