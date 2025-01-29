import sys
result = []
for s in sys.stdin:
    beds = s.strip()
    empty = []
    count = 0
    for bed in beds:
        if bed == "X":
            empty.append(count)
            count = 0
        else:
            count += 1
    if count != 0:
        empty.append(count)
    if empty[0] == 0:
        empty.pop(0)
    max_d = 0
    if beds[0] == '.': 
        max_d = max(max_d, empty.pop(0) - 1)
    if beds[-1] == '.':
        max_d = max(max_d, empty.pop() - 1)

    for dist in empty:
        max_d = max(max_d, (dist - 1) // 2)

    result.append(str(max_d))
sys.stdout.write("\n".join(result)+"\n")
            
