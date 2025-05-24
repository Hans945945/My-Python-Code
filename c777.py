n,m = map(int, input().split())
a = [1,2,3]
while a[-1] < n:
    a.append(a[-3]+a[-2]+a[-1])
count = 0 + (4-n)*(n<=3)
while a[-1] < m:
    a.append(a[-3]+a[-2]+a[-1])
    count += 1
print(count)
