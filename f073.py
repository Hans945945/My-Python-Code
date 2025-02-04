n = int(input())
cards = input().split()
k = int(input())
print(" ".join(cards[k:]), " ".join(cards[:k]))
