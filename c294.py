a,b,c = map(int, input().split())
if a>b:
    temp = a
    a = b
    b = temp
if b>c:
    temp = b
    b = c
    c = temp
if a>b:
    temp = a
    a = b
    b = temp
print(a,b,c)
if a+b<=c:
    print("No")
elif a*a+b*b < c*c:
    print("Obtuse")
elif a*a+b*b == c*c:
    print("Right")
elif a*a+b*b > c*c:
    print("Acute")
