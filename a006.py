a,b,c = map(int, input().split())
if b**2 - 4*a*c < 0:
    print("No real root")
elif b**2 - 4*a*c == 0:
    x = -1*b//(2*a)
    print("Two same roots x="+str(x))
else:
    x1 = (-1*b + (b**2 - 4*a*c)**0.5) // (2*a)
    x2 = (-1*b - (b**2 - 4*a*c)**0.5) // (2*a)
    print("Two different roots x1="+str(int(x1)),", x2="+str(int(x2)))
