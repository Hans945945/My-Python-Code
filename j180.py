import sys
import math
data = sys.stdin.read().splitlines()
r = []
for s in data[:-1]:
    n,e = map(int, s.split())
    foods = n*e
    days = 0
    while n > 1:
        day = math.ceil((foods-(n-1)*e)/n)
        days += day
        foods -= day*n
        n -= 1
    days += foods
    r.append(days)
sys.stdout.write("\n".join(map(str, r))+"\n")
        
