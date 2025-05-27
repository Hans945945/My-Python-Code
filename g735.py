N = int(input())
scores = list(map(int, input().split()))
temp = sorted(scores, reverse = True)
last = temp[0]
rank = 1
ranking = {last:"1"}
count = 1
for n in temp[1:]:
    count += 1
    if n < last:
        rank = count
    ranking[n] = str(rank)
    last = n
print(" ".join(ranking[s] for s in scores))
    
