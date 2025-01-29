h,m = map(int, input().split(":"))
while not(h == 0 and m == 0):
    h = h*30 + m*0.5
    m = m*6
    print(f"{min(abs(h-m),360-abs(h-m)):.3f}")
    h,m = map(int, input().split(":"))
    
    
