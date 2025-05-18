import sys
data = sys.stdin.readlines()
n,k = map(int, data[0].split())
cards = [s.rstrip() for s in data[1:]]
print("\n".join(cards[k:]), "\n".join(cards[:k]), sep = "\n")
