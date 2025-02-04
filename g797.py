import sys
n,m = map(int, sys.stdin.readline().split())
half = n//2
cards = sys.stdin.readline().split()
for _ in range(m):
    left = cards[:half]
    right = cards[half:]
    cards = [left[i//2]if i%2 == 0 else right[i//2] for i in range(n)]
sys.stdout.write(" ".join(cards)+"\n")
