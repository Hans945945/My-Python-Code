import sys

r = []
for s in sys.stdin.readlines():
    n = int(s)
    level = 1
    while n > (level * (level + 1)) // 2:
        level += 1
    
    pos = n - (level * (level - 1)) // 2 - 1
    if level % 2:
        x, y = level - pos, 1 + pos
    else:
        x, y = 1 + pos, level - pos

    r.append(f"TERM {n} IS {x}/{y}")
sys.stdout.write("\n".join(r)+"\n")

