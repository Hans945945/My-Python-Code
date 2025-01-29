def GCD(a,b):
    while b:
        a,b = b,a%b
    return a
n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    m = len(nums)
    biggest = 0
    for i in range(m):
        for j in range(i,m):
            r = GCD(nums[i],nums[j])
            if r > biggest and i != j:
                biggest = r
    print(biggest)
