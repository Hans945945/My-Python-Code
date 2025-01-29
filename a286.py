import sys
data = sys.stdin.read().splitlines()
index = 0
r = []
while index < len(data):
    girl = sum(map(int, list(data[index].replace(" ",""))))
    while girl > 9:
        girl = sum(map(int, list(str(girl))))
    index += 1
    n = int(data[index])
    index += 1
    closest = 10
    winner = 0
    for i in range(1, n+1):
        boy = sum(map(int, list(data[index].replace(" ",""))))
        index += 1
        while boy > 9:
            boy = sum(map(int, list(str(boy))))
        if abs(girl-boy) < closest:
            closest = abs(girl-boy)
            winner = str(i)
    r.append(winner)
sys.stdout.write("\n".join(r)+"\n")
