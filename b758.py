x,y = map(int, input().split())
e = x*60+y+150
m = e%60
h = e//60
if h >= 24:
    h = h%24
if h<10:
    h = "0"+str(h)
if m <10:
     m = "0"+str(m)
print(str(h)+":"+str(m))
