import sys
n = int(sys.stdin.readline())
players = sys.stdin.readline().split()
elims = []
data = sys.stdin.read().splitlines()
for s in data[:-1]:
    players[int(s)-1] = "0"
    elims.append(s)

if len(elims) != len(set(elims)):
    print("Wrong")
else:
    print("Werewolves" if "-1" in players else "Townsfolk")
