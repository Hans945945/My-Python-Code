T = int(input())
score = []
for i in range(T):
    a = int(input())
    b = int(input())
    j = 1
    count = 0
    while j**2 < b:
        count = count + j**2
        j = j+1
    j = 1
    while j**2 < a:
        count = count- j**2
        j = j+1
    score.append(count)
for s in range(T):
    print("Case",str(s+1)+":", score[s])
