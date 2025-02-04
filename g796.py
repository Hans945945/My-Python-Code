import sys
from collections import Counter
n = int(sys.stdin.readline())
files = []
for s in sys.stdin:
    num = int(s[3:6])
    files.append(num//10)
sys.stdout.write("\n".join(f"{key} {value}" for key, value in sorted(Counter(files).items())))
