n = int(input())
for _ in range(n):
    h,m,s = map(int, input().split())
    s += h*32*16 + m*16
    earth_s = s *4
    earth_m = earth_s // 60
    earth_s = earth_s % 60
    earth_h = earth_m // 60
    earth_m = earth_m % 60
    print(f"{earth_h}:{earth_m}:{earth_s}")
    
