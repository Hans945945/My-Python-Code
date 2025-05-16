import sys
servants = ["Saber", "Lancer", "Archer", "Rider", "Caster", "Assassin", "Berserker"]
scores = [0] * 7

for s in sys.stdin:
    for ch in s:
        if ch.isalpha():
            scores[(ord(ch.upper()) - ord('A')) % 7] += 1
ans = 0
for i in range(1, 7):
    if scores[i] > scores[ans]:
        ans = i

print(servants[ans])
