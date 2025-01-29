T = int(input())
for _ in range(T):
    h,m = map(int, input().split(":"))
    m += h*60
    m = ((720-m) % 720) *(m != 720)
    h = m // 60
    h += 12*(h == 0)
    m %= 60
    print(f"{h:02}:{m:02}")
    
