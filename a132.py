import sys
data = sys.stdin.read().splitlines()[:-1]
for s in data:
    n = format(int(s), 'b')
    r = n.count("1")
    sys.stdout.write(f'The parity of {n} is {r} (mod 2).'+"\n")
