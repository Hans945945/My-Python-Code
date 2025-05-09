import sys
count = 0
max_n = 0
for s in sys.stdin.readlines()[1:]:
    _,c = map(int, s.split())
    count += (c == 1)-(c == 0)
    max_n = max(count, max_n)
print(max_n)
