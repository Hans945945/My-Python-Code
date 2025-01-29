'''
while True:
    n = input()
    if n == "0":
        break
    while len(n) != 1:
        total = 0
        for i in n:
            total += int(i)
        n = str(total)
    print(n)
'''
import sys
for s in sys.stdin:
    if s.rstrip() == "0":
        break
    print(int(s)%9 if int(s)%9 != 0 else 9)
