import sys
r = []
for s in sys.stdin.readlines():
    if not s.strip():
        continue
    parts = s.rstrip().split('-')
    digits = ''.join(parts[:-1]) 
    count = 0
    
    for i in range(9):
        count += int(digits[i]) * (i + 1)

    n = count % 11
    check = 'X' if n == 10 else str(n)

    r.append("Right" if check == parts[-1] else f"{parts[0]}-{parts[1]}-{parts[2]}-{check}")
sys.stdout.write("\n".join(r)+"\n")

