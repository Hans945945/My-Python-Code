from math import log
n = input()
print(f"{log(log(int(n[:15])) + 2.3025850929*(len(n)-15)) + 0.2614972128476428:.3f}")
