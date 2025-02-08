import sys
from functools import reduce
from math import gcd
'''
def lcm(a,b):
    total = abs(a*b)
    while b:
        a,b = b, a % b
    return total // a
'''
def lcm(a,b):
    return abs(a * b) // gcd(a, b)
data = sys.stdin.readlines()[:-1]
r = []
for i in range(1,len(data),2):
    nums = list(map(int, data[i].split()))
    r.append(reduce(lcm,nums))
sys.stdout.write("\n".join(map(str,r))+"\n")
    
