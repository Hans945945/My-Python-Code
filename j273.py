import sys
from collections import Counter
n = int(sys.stdin.readline())
sys.stdout.write("\n".join(f"{Id} {time}" for Id, time in sorted(Counter(sys.stdin.readline().split()).items()))+"\n")
