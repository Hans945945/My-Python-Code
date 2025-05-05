scores = list(map(int, input().split()))
for s in scores:
    bars = list(map(int, input().split()))
    print("X" if s == 0 else "A" if s >= bars[0] else "B" if s >= bars[1] else "C" if s >= bars[2] else "D" if s >= bars[3] else "E" if s >= bars[4] else "F")
