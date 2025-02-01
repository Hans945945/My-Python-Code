import sys
from collections import defaultdict
square_dict = defaultdict(list)
for i in range(34, 100000):
    square = i * i
    square_str = str(square)
    if '0' in square_str:
        continue
    sorted_square = "".join(sorted(square_str))
    square_dict[sorted_square].append(str(square))
result = []
for line in sys.stdin:
    line = line.strip()
    sorted_line = "".join(sorted(line))
    if sorted_line in square_dict:
        result.append(" ".join(sorted(square_dict[sorted_line])))
    else:
        result.append("0")
sys.stdout.write("\n".join(result) + "\n")
