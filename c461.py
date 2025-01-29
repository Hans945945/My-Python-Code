a,b,r = map(bool, map(int, input().split()))
i = True
if (a and b) == r:
    print("AND")
    i = False
if (a or b) == r:
    print("OR")
    i = False
if (a^b) == r:
    print("XOR")
    i = False
if i:
    print("IMPOSSIBLE")


