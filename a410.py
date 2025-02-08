a,b,c,d,e,f = map(int, input().split())
a2 = a*d
b2 = b*d
c2 = c*d
d2 = d*a
e2 = e*a
f2 = f*a
if (a2 == d2 and b2 == e2 and c2 == f2):
    print("Too many")
elif a2 == d2 and b2 == e2 and c2 != f2:
    print("No answer")
elif a == 0:
    y = c/b
    x = (f-e*y)/d
    print('x='+str(format(x,'.2f')))
    print('y='+str(format(y,'.2f')))
else:
    y = (c2-f2)/(b2-e2)
    x = (c-b*y)/a
    print('x='+str(format(x,'.2f')))
    print('y='+str(format(y,'.2f')))

