import sys
T = int(input())
count = 0
for s in sys.stdin:
    if "商店" in s:
        count += 1
print(count)
