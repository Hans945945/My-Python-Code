n = int(input())
r = int(input())
MAP = [set() for _ in range(n+1)]
for _ in range(r):
    x,y = map(int, input().split())
    MAP[x].add(y)
    MAP[y].add(x)
k = int(input())
for _ in range(k):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        print(len(MAP[temp[1]]))
    else:
        print("Yes" if temp[2] in MAP[temp[1]] else "No")
