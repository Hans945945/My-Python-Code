n = int(input())
for _ in range(n):
    a,b,c,d,e,f = map(int, input().split())
    if a == 0:
        y = c//b
        x = (f-e*y)//d
    elif d == 0:
        y = f//e
        x = (c-b*y)//a
    else:
        b,e = b*d, e*a
        c,f = c*d, f*a
        a,d = a*d, d*a
        y = (c-f)//(b-e)
        x = (c-b*y)//a
    print(x,y)
