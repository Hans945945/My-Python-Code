import sys
r = []
c = 0
table = ["十六夜", "紅美鈴", "帕秋莉·諾雷姬"]
people = {"十六夜": 0, "紅美鈴": 0, "帕秋莉·諾雷姬": 0}
who_wins = { "Scissors Stone": 1, "Paper Stone": 0, "Scissors Paper": 0, "Paper Scissors": 1, "Stone Scissors": 0, "Stone Paper": 1 }
for s in sys.stdin.readlines()[:-2]:
    c += 1
    data = s.strip().split(",")
    same = list(set(data))
    flag = 1
    for i in range(3):
        if data[i] not in ["Scissors", "Stone", "Paper"]:
            p = table[i]
            r.append(f"{p}贏了第{c}局的比賽")
            people[p] += 1
            flag = 0
            break
    if flag:
        if len(same) == 3 or len(same) == 1:
            r.append(f"第{c}局不分勝負")
        else:
            if data.count(same[0]) < data.count(same[1]):
                same[0], same[1] = same[1], same[0]
            p = data.index(same[1])
            winner = table[p]
            if who_wins[f"{same[0]} {same[1]}"]:
                r.append(f"{winner}贏了第{c}局的比賽")
                people[winner] += 1
            else:
                for i in range(3):
                    people[table[i]] += 1
                people[winner] -= 1
                r.append(f"{winner}輸了第{c}局的比賽")

r.append(f"十六夜總計贏了{people['十六夜']}局比賽")
r.append(f"紅美鈴總計贏了{people['紅美鈴']}局比賽")
r.append(f"帕秋莉·諾雷姬總計贏了{people['帕秋莉·諾雷姬']}局比賽")
r.append("趕上旅程" if people["十六夜"] > people["紅美鈴"] and people["十六夜"] > people["帕秋莉·諾雷姬"] else "繼續做家事")
sys.stdout.write("\n".join(r) + "\n")
