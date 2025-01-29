import sys
data = sys.stdin.read().splitlines()
index = 0
r = []
while index < len(data):
    name, w, h, orders = data[index].split()
    h = int(h)
    r.append(name)
    index += 1
    stars = [list(data[i]) for i in range(index, index+h)]
    index += h
    if orders.count("I")%2:
        stars.reverse()
    if orders.count("R")%2:
        for row in stars:
            row.reverse()
    r.extend("".join(row) for row in stars)
sys.stdout.write("\n".join(r))
