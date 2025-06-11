import sys
for s in sys.stdin.readlines()[1:]:
    a, b = s.split()
    print(hex(int(a, 8) + int(b, 8))[2:].upper())
