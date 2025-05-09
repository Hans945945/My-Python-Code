n = int(input())
price = list(map(int, input().split()))
t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    print(price[a]+price[b])
