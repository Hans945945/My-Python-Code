import sys
def hanoi(n, source, temp, target):
    if n == 1:
        print(f"Move ring 1 from {source} to {target}")
    else:
        hanoi(n - 1, source, target, temp)
        print(f"Move ring {n} from {source} to {target}")
        hanoi(n - 1, temp, source, target)

for s in sys.stdin:
    hanoi(int(s),"A","B","C")
    print()
