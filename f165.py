a,b = map(int,input().split())
if b == 0:
    print("OK!")
else:
    r = a%b
    if r == 0:
        print("OK!")
    else:
        print(r)
