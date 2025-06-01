data = list(map(int, input().split()))
n,y = data[0],data[1]
sprays = data[2:]
target = sprays[0] + y
total = 0

for i in range(n):
    t,x = sprays[2*i],sprays[2*i + 1]
    if t <= target:
        total += max(0, x - (target - t))

print(total)
