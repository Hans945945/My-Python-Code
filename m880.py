import sys
data = sys.stdin.readlines()
old = data[0].split()
n = int(data[1])
for i in range(n):
    a,b = map(int, data[2+i].split())
    old[a],old[b] = old[b],old[a]
picks = data[-1].split()
sys.stdout.write(" ".join(old)+"\n")
sys.stdout.write(str(picks.index(str(old.index("Joker")))+1)+"\n")
