cards = list(input())
goal = input()
r = []
for letter in goal:
    if letter not in cards:
        r.append("X")
    else:
        temp = cards.index(letter)
        r.append(temp+1)
        cards[temp] = 0
print(" ".join(map(str, r)))
        
