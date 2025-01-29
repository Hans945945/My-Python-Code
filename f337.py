n,m = map(int, input().split())
if n*3 < m*8:
    print("Too much")
elif n*2 > m*8:
    print("Not enough")
else:
    print("Yes")
