import sys
for s in sys.stdin.readlines():
    print(int(s)+int(s[::-1]))
