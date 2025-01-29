import sys
n, P = sys.stdin.readline().strip().split()
P = list(map(int, list(P)))
n = int(n)
P = P[::-1]
max_score = 0
team = ""
for i in range(0,len(P),n):
    if sum(P[i:i+n]) >= max_score:
        max_score = sum(P[i:i+n])
        team = i//n+1
    
sys.stdout.write(f"{team} {max_score}\n")
