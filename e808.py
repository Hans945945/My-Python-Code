n = int(input())
h,m = map(int, input().split())
m = h*60+m
time = [m]
for _ in range(n):
    t = int(input())
    m += t
    time.append(m)
s = list(map(int, input().split()))
s.pop()
for i in range(len(s)):
    h = (time[s[i]] // 60)%24
    m = time[s[i]]%60
    if h < 10:
        h = "0"+str(h)
    if m < 10:
        m = "0"+str(m)
    print(f'{h}:{m}')
