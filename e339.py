from itertools import accumulate
n = int(input())
print(" ".join(map(str, accumulate(map(int, input().split())))))
