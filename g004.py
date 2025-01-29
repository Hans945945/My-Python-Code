import sys

r,c = map(int, sys.stdin.readline().split())
now = [list(map(int, s.split())) for s in sys.stdin]
result = [row[:] for row in now]
for i in range(r):
    for j in range(c):
        if now[i][j] == 0:
            total= 0
            count = 0
            if i > 0 and now[i-1][j] != 0:
                total += now[i-1][j]
                count += 1
            if i < r-1 and now[i+1][j] != 0:
                total += now[i+1][j]
                count += 1
            if j > 0 and now[i][j-1] != 0:
                total += now[i][j-1]
                count += 1
            if j < c-1 and now[i][j+1] != 0:
                total += now[i][j+1]
                count += 1
                
            result[i][j] = total // count if count else 0
result = [" ".join(map(str, row)) for row in result]
sys.stdout.write("\n".join(result))
