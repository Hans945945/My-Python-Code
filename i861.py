N = int(input())
nums = list(map(int, input().split()[:-1]))
for n in nums:
    print(n*N, end = " ")
    N-=1
