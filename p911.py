cards = input().split()
count = {"S":0, "H":0,"D":0,"C":0}
points = 0
for card in cards:
    count[card[0]] += 1
    if card[1] == "A":
        points += 4
    elif card[1] == "K":
        points += 3
    elif card[1] == "Q":
        points += 2
    elif card[1] == "J":
        points += 1
print(" ".join(map(str, count.values())))
print(points)
