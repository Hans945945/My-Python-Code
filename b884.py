n = int(input())
for _ in range(n):
    x,y = map(int, input().split())
    r = (x+y)**0.5
    yee = 100-r*r
    if yee <= 0:
        print("evil!!")
    elif yee <= 30:
        print("sad!")
    elif yee <= 60:
        print("hmm~~")
    elif yee < 100:
        print("Happyyummy")
    else:
        print("evil!!")
    
