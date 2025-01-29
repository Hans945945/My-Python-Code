n = int(input())
s = [9999999]
for i in range(n):
    data = list(input())
    g = []
    for j in range(len(data)):
        if g.count(data[j]) == 0:
            g.append(data[j])
    if len(g) < s[0]:
        del s[0:len(s)]
        s.append(len(g))
        s.append(data)
    elif len(g) == s[0]:
        s.append(data)
b_n = [0]
if len(s) >2:
    for i in range(len(s)):
        b_n[0] = 100
        Next = False
        for j in range(1,len(s)):
            if ord(s[j][i])<b_n[0]:
                del b_n[0:len(b_n)]
                b_n.append(ord(s[j][i]))
                b_n.append(s[j])
            elif ord(s[j][i]) == b_n[0]:
                b_n.append(s[j])
                Next = True
        if not Next:
            break
    print(''.join(b_n[1]))
else:
    print(''.join(s[1]))
            
        

