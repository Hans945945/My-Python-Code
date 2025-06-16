from collections import Counter
m,n,k = map(int, input().split())
wheels = [list(input()) for _ in range(m)]
total = 0
for _ in range(k):
    temp = list(map(int, input().split()))
    for i in range(m):
        if temp[i] > 0:
            now = wheels[i]*2
            wheels[i] = now[n-temp[i]%n: n-temp[i]%n+n]
        elif temp[i] < 0:
            now = wheels[i]*2
            wheels[i] = now[-temp[i]%n: -temp[i]%n+n]
    temp = list(zip(*wheels))
    for t in temp:
        total += max(Counter(t).values())
print(total)
