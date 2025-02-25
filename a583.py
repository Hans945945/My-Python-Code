n,m = map(int, input().split())
students = list(map(int, input().split()))
for i in range(0,m*2,2):
    students.append((students[i],students[i+1]))
del students[:m*2]
closest = float("inf")
for i in range(m):
    for j in range(i+1,m):
        x1,y1 = students[i]
        x2,y2 = students[j]
        closest = min((x1-x2)**2+(y1-y2)**2,closest)
print(f"{closest**0.5:.4f}")
