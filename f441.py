n,s = map(int, input().split())
ans = input().replace(" ","")
m = int(input())
for _ in range(m):
    score = 0
    test = input().replace(" ","")
    for i in range(n):
        if ans[i] == test[i]:
            score += 1
    print(score*s)
