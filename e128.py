import sys
import math
r = []
for s in sys.stdin.readlines()[:-1]:
    n = int(s)
    temp = math.ceil(n**0.5)
    sign = temp * temp - temp + 1
    x = y = temp
    if n < sign and temp%2 == 0:
        x = temp - sign + n
    elif n > sign and temp%2 == 1:
        x = temp - n + sign
    elif n > sign and temp%2 == 0:
        y = temp - n + sign
    elif n < sign and temp%2 == 1:
        y = temp - sign + n
    r.append(f"{x} {y}")
sys.stdout.write("\n".join(r)+"\n")
