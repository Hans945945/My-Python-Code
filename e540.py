T = int(input())
for _ in range(T):
    Qs = input()
    streak = 0
    score = 0
    for q in Qs:
        if q == "O":
            streak += 1
            score += streak
        else:
            streak = 0
    print(score)
