import math
while True:
    try:
        n,P = map(int, input().split())
        if n >= P:
            print(0)
        else:
            print(pow(math.factorial(n),1,P))
    except EOFError:
        break
