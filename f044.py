import math
n, t = map(int, input().split())
if t == 0:
    print(0)
else:
    print(int(math.log2(t / n +1)))



