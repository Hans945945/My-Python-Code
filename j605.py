k = int(input())
time = []
s = []
sm = 0
for _ in range(k):
    t,i = list(map(int, input().split()))
    if i == -1:
        sm += 1
    time.append([i,t*-1])
    s.append(i)
    time.sort(reverse = True)
final = max(s) - k - 2*sm
if final > 0:
    print(final, time[0][1]*-1)
else:
    print(0,time[0][1]*-1)
