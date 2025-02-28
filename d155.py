import sys
c1 = 0
c2 = 0
r = []
who_wins = {"Scissors Stone":1, "Paper Stone":0, "Scissors Paper":0, "Paper Scissors":1,"Stone Scissors":0, "Stone Paper":1}
for s in sys.stdin.readlines()[:-1]:
    if who_wins[s.strip()]:
        c2 += 1
        r.append("靈夢獲勝")
    else:
        c1 += 1
        r.append("紫獲勝")
r.append("悲慘的籌措起香油錢" if c2>c1 else "螢火的蹤跡")
sys.stdout.write("\n".join(r)+"\n")
