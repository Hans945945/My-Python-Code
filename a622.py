teams = []
length = []
while True:
    team = input()
    if team == "END":
        break
    teams.append(team)
    length.append(len(team))
longest = max(length)
for i in range(len(teams)):
    while len(teams[i]) < longest:
        teams[i]+=" "
for i in range(longest):
    print("  ".join(teams[j][i] for j in range(len(teams))))
                   
