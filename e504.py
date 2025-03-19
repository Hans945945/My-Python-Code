import sys
r = []
table = {"W":1, "H":0.5, "Q":0.25, "E":1/8, "S":1/16, "T":1/32, "X":1/64}
for s in sys.stdin.readlines()[:-1]:
    sections = s.split("/")
    count = 0
    for notes in sections:
        if sum(table[n] for n in notes.strip()) == 1:
            count += 1
    r.append(count)
sys.stdout.write("\n".join(map(str, r))+"\n")
