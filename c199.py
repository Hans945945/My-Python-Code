m = list(map(int, input().split()))
n = m.pop(0)
count = 0
s = "d"
for i in range(1,n):
    if s == "u" and m[i] < m[i-1]:
        count += 1
        s = "d"
    elif s == "d" and m[i] > m[i-1]:
        s = "u"
print(count)
        
