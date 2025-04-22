import sys
from itertools import combinations

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

r = []
data = sys.stdin.readlines()[:-1]
idx = 0
while idx < len(data):
    n = int(data[idx])
    idx += 1
    nums =[int(data[idx+i]) for i in range(n)]
    idx += n
    count = sum(1 for a,b in combinations(nums,2) if gcd(a,b) == 1)
    r.append(f"{(3*n*(n-1)/count)**0.5:.6f}" if count != 0 else "No estimate for this data set.")
sys.stdout.write("\n".join(r)+"\n")
    
    
        
    
