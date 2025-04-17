n = int(input())
lens = list(map(int, input().split()))
w = list(map(int, input().split()))
lens.sort(reverse = True)
gift = 0
ans = 0
for i in range(1,n):
    gift += w[i-1]
    ans += lens[i]*gift
print(ans)
    
