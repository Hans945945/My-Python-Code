def GCD(a,b):
    while b:
        a,b = b, a%b
    return a
while True:
    try:
        a,b = map(int,input().split())
        print(GCD(a,b))
    except:
        break
