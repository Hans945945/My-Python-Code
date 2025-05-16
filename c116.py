import math
import sys
for s in sys.stdin:
    x1, y1, x2, y2, x3, y3 = map(float, s.split())
    
    a = math.hypot(x2 - x1, y2 - y1)
    b = math.hypot(x3 - x2, y3 - y2)
    c = math.hypot(x3 - x1, y3 - y1)

    A = abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)) / 2
    
    print(f"{2 * math.pi * (a * b * c) / (4 * A) :.2f}")
