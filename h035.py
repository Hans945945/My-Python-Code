nine = [0 for i in range(10)]
wait = [0 for i in range(10)]
scores = [0 for i in range(10)]
n = int(input())
pitches = list(map(int, input().split()))
score = 0
flag = True
for i in range(n):
    for j in range(1,10):
        if wait[j] == 12:
            nine[j] = 0
            wait[j] = 0
        if wait[j] != 0:
            wait[j] += 1
    if pitches[i] == -1:
        continue        
    nine[pitches[i]] = 1
    if wait[pitches[i]] == 0:
        wait[pitches[i]] = 1
        if scores[pitches[i]] == 0:
            score += pitches[i]
            scores[pitches[i]] = 1
    if nine[1:].count(0) == 0:
        print("perfect")
        flag = False
        break
if flag:      
    print(score)
    
    
    
