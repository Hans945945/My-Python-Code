import sys
from itertools import permutations
for s in sys.stdin.readlines()[:-1]:
    N = int(s)
    if N < 10:
        nums = permutations("0123456789",5)
    else:
        nums = permutations("123456789",4)
    r = []
    for n in nums:
        n = "0"*(N>=10) + "".join(n)
        temp = str(int(n)*N)+n
        if len(temp) == 10 and len(set(temp)) == 10:
            r.append(f"{temp[:5]} / {n} = {N}")
    print("\n".join(r)+"\n" if r else f"There are no solutions for {N}.\n")
