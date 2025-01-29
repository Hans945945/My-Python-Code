import sys
original = sys.stdin.readline().strip()
b = original.upper()
c = original.title()
d = original.lower()
a = b[0] + d[1:]
sys.stdout.write(f"{a}\n{b}\n{c}\n{d}\n")

