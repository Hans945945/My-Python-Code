import sys
from itertools import permutations

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for p in permutations(sorted(nums)):
    sys.stdout.write(" ".join(map(str, p))+"\n")
    
