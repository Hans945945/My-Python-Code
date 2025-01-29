import sys
n = int(sys.stdin.readline())
chickens = sys.stdin.readline().split()
e = sys.stdin.readline().strip()
q = int(sys.stdin.readline())

for caught in sys.stdin.readline().split():
    chickens[chickens.index(caught)], e = e, chickens[chickens.index(caught)]
sys.stdout.write(" ".join(chickens) + "\n")


    
