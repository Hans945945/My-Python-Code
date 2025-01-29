def factors(n):
    nums = []
    if n == 1:
        return [1]
    while n != 1:
        for i in range(9,0,-1):
            if i == 1:
                return -1
            elif n % i == 0:
                n //= i
                nums.append(i)
                break
    nums.reverse()
    return nums
T = int(input())
for _ in range(T):
    n = int(input())
    r = factors(n)
    if r == -1:
        print(-1)
    else:
        print("".join(list(map(str, r))))
