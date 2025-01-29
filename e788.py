N = int(input())
p = []
for _ in range(N):
    array = list(input().split())
    a = array[0][0]
    array[0] = array[0][1:len(array[0])]
    code = array[0][len(array[0])-1]
    array[0] = array[0][:len(array[0])-1]
    array.insert(1,code)
    array.insert(0,a)
    array.append(ord(array[2]))

    p.append(array)

for i in range(N-1):
    for j in range(N-i-1):
        if p[j][4] > p[j+1][4]:
            temp = p.pop(j)
            p.insert(j,p[j])
            p.pop(j+1)
            p.insert(j+1,temp)
        if int(p[j][0]) > int(p[j+1][0]) and p[j][2] == p[j+1][2]:
            temp = p.pop(j)
            p.insert(j,p[j])
            p.pop(j+1)
            p.insert(j+1,temp)

for k in range(N):
    print(p[k][2]+": "+p[k][3])

