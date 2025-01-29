b,N = map(int, input().split())
n_10 = int(str(N),b)
N = list(map(int, list(str(N))))
nums = [N[i]**len(N) for i in range(len(N))]

if sum(nums) == n_10:
    print("YES")
else:
    print("NO")

