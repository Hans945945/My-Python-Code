n = int(input())
ds = []
for _ in range(n):
    d = list(map(int, input().split()))
    ds.append(d)
ds.sort()
for i in range(n):
    print(ds[i][0], ds[i][1])
    

