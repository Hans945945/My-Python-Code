import math
import sys
ans = []
for n in range(2, 13):
    ans.append(f"{int(math.factorial(n)/math.e+0.5)}/{math.factorial(n)}")
input()
for s in sys.stdin:
    sys.stdout.write(ans[int(s)-2]+"\n")
