import sys
def factors(n):
    total = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            total += i
            if i != n**0.5:
                total += n//i
    return total-n
nums = list(map(int, sys.stdin.read().split()))
i = 0
print("PERFECTION OUTPUT")
while True:
    n = nums[i]
    if n == 0:
        break
    print("".join([" " for _ in range(5-len(str(n)))])+str(n), end = "  ")
    total = factors(n)
    if n == total:
        print("PERFECT")
    elif n < total:
        print("ABUNDANT")
    else:
        print("DEFICIENT")
    i+=1
print("END OF OUTPUT")
