l = input().split()
n = int(l[0])
m = int(l[1])

for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = a+b
    count = 0
    c.sort()

    for x in range(len(c)-1):
        if c[x] == c[x+1]:
            count += 1
    print(count)
    
