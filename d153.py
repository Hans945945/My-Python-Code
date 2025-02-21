import sys
data = sys.stdin.readlines()[1:]
index = 0
r = []
while index < len(data):
    n = int(data[index])
    index += 1
    if n % 2 == 0:
        idx = n//2 - 1
    else:
        idx = (n+1)//2-1
    cows = list(map(int, data[index:index + n]))
    index += n
    cows.sort()
    r.append(cows[idx])
sys.stdout.write("\n".join(map(str, r))+"\n")
        
