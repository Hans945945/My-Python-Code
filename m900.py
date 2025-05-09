R,G,B = map(int, input().split())
r,g,b = R/255, G/255, B/255
Max = max(r,g,b)
Min = min(r,g,b)
l = (Max+Min)/2
if Max == Min:
    h = 0
elif Max == r:
    h = 60*(g-b)/(Max-Min) + 360*(g<b)
elif Max == g:
    h = 60*(b-r)/(Max-Min) + 120
else:
    h = 60*(r-g)/(Max-Min) + 240
if l == 0 or Max == Min:
    s = 0
elif l <= 0.5:
    s = (Max-Min)/(2*l)
else:
    s = (Max-Min)/(2-2*l)
print(f"{h:.0f} {s*255:.0f} {l*255:.0f}")
