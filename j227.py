from collections import Counter
import sys
need = sys.stdin.readline().strip().split()
get = Counter(sys.stdin.readline().strip().split())
sys.stdout.write(f"{min(get.get(n,0) for n in need)}\n")
