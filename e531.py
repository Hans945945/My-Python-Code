import sys
notes = {
    "c": "0111001111",
    "d": "0111001110",
    "e": "0111001100",
    "f": "0111001000",
    "g": "0111000000",
    "a": "0110000000",
    "b": "0100000000",
    "C": "0010000000",
    "D": "1111001110",
    "E": "1111001100",
    "F": "1111001000",
    "G": "1111000000",
    "A": "1110000000",
    "B": "1100000000"
}
data = sys.stdin.readlines()[1:]
r = []
for s in data:
    keys = s.strip()
    count = {i:0 for i in range(10)}
    if not keys:
        r.append(" ".join(map(str, count.values())))
        continue
    old = "0000000000"
    for w in keys:
        now = notes[w]
        for i in range(10):
            if old[i] < now[i]:
                count[i] += 1
        old = now
    r.append(" ".join(map(str, count.values())))
sys.stdout.write("\n".join(r)+"\n")
