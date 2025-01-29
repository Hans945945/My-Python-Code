def f(n):
    if n == 1:
        return 
    else:
        for j in range(2,n+1):
            if n%j == 0:
                factors.append(j)
                return f(n//j)
N = int(input())
factors = []
f(N)
while len(factors):
    if factors.count(factors[0]) == len(factors):
        end = ""
    else:
        end = " * "
    if factors.count(factors[0]) == 1:
        print(factors[0], end = end)
        factors.pop(0)
    else:
        print(str(factors[0])+"^"+str(factors.count(factors[0])),end = end)
        del factors[0:factors.count(factors[0])]
