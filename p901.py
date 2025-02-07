import sys
data = sys.stdin.read().split()
n = int(data[0])
need = data[1:n+1]
r, c = map(int, data[n+1:n+3])
shelf = data[n+3:]

position_map = {item: (i//c+1, i%c+1) for i, item in enumerate(shelf)}

result = [f"{position_map[item][0]} {position_map[item][1]}" if item in position_map else "-1" for item in need]
sys.stdout.write("\n".join(result) + "\n") 
