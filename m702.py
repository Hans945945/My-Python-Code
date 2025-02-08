import sys
from collections import Counter
from heapq import nlargest
n,m = map(int, sys.stdin.readline().split())
votes = Counter(sys.stdin.read().split())
sys.stdout.write(" ".join(nlargest(m, votes.keys(), key=lambda x: (votes[x], x)))+"\n")
    
