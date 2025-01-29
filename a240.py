'''
T = int(input())
for _ in range(T):
    N = int(input())
    a,b = 1, 17
    a = a* 10**N
    r = str(a//b).zfill(N+1)
    print(r[-1], sum(map(int, r[1:])))
'''
T = int(input())
nums = [0, 5, 8, 8, 2, 3, 5, 2, 9, 4, 1, 1, 7, 6, 4, 7]
cycle_len = 16
for _ in range(T):
    n = int(input())
    print(nums[(n-1) % cycle_len], sum(nums[:n % cycle_len]) + 72*(n // cycle_len))
    
    
