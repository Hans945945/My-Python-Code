n = int(input())
for k in range(n):
    rating = []
    for i in range(10):
        web, rate = input().split()
        rate = int(rate)
        rating.append([rate,10-i,web])
    rating.sort(reverse = True)
    highest = rating[0][0]
    print(f"Case #{k+1}:")
    j = 0
    while rating[j][0] == highest:
        print(rating[j][2])
        j+=1
        if j==len(rating):
            break
    
        
