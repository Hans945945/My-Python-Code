data = [(3,4,5),(5,12,13),(7,24,25),(8,15,17),(20,21,29),(9,40,41)]
for a,b,c in data:
    if 1000 % (a+b+c) == 0:
        times = 1000 // (a+b+c)
        print(a*b*c*times**3)
