import sys
n = int(sys.stdin.readline())
rain = list(map(int, sys.stdin.readline().split()))
sun = list(map(int, sys.stdin.readline().split()))
rain_need, sun_need = map(int, sys.stdin.readline().split())
total_rain = 0
total_sun = 0
r = -1
for i in range(n):
    total_rain += rain[i]
    total_sun += sun[i]
    if total_rain >= rain_need and total_sun >= sun_need:
        r = i+2
        break
print(r)
