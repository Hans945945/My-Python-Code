s = []
for _ in range(3):
    a,b = map(int, input().split())
    s.append((a,b))
s.sort()
flag = 0
for i in range(1,3):
    if s[i][0]< s[i-1][1]:
        flag = 1
        break
print("QQ" if flag else "Happy")
    
