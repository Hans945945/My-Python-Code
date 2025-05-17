import sys
data = sys.stdin.readlines()[:-1]
for i in range(0,len(data),2):
    nums = list(map(int, data[i+1].split()))
    b = 0
    ans = 0
    for n in nums:
        b += n
        ans += abs(b)
    print(ans)
    
