m = int(input())
for _ in range(m):
    a,b,c = map(int, input().split())
    n = b**2 - 4*a*c
    if n < 0:
        print("No")
        continue
    r = n**0.5
    if int(r) == r:
        print("Yes")
    else:
        print("No")
        
