points = (1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10)
N = int(input())
bonus = []
for _ in range(N):
    bonus.append(input().split())
M = int(input())
for _ in range(M):
    word, y, x, d = map(str, input().split())
    x = int(x)-1
    y = int(y)-1
    score = 0
    extra = []
    for letter in word:
        score += points[ord(letter)-65]
    if d == "H":
        d = x
    else:
        d = y
    for i in range(d,len(word)+d):
        if d == x:
            if bonus[y][i] != "[]":
                if bonus[y][i] == "2L":
                    score += points[ord(word[i-d])-65]
                elif bonus[y][i] == "3L":
                    score += 2 * points[ord(word[i-d])-65]
                else:
                    extra.append(bonus[y][i])
        else:
            if bonus[i][x] != "[]":
                if bonus[i][x] == "2L":
                    score += points[ord(word[i-d])-65]
                elif bonus[i][x] == "3L":
                    score += 2 * points[ord(word[i-d])-65]
                else:
                    extra.append(bonus[i][x])
    for j in extra:
        if j == "3W":
            score *= 3
        else:
            score *= 2
    print(word, score)
        
    
