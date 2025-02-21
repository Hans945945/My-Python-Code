import sys
r = []
for s in sys.stdin.readlines():
    r.append(sum(map(int, s.split()))*2)
sys.stdout.write("\n".join(map(str, r))+"\n")
    
