month = (31,28,31,30,31,30,31,31,30,31,30,31)
m1,d1 = map(int, input().split())
m2,d2 = map(int, input().split())
for i in range(m1-1):
    d1+=month[i]
for i in range(m2-1):
    d2+=month[i]
if d1>d2:
    print(365-(d1-d2))
elif d1 <= d2:
    print(d2-d1)

