import sys
board = [["-" for _ in range(10)] for _ in range(10)]
i = 0
for s in sys.stdin:
    i+=1
    data = s.strip()
    middle = data.index(",")
    y,x = int(data[1:middle]), int(data[middle+1:len(data)-1])
    board[y-1][x-1] = str(i)
board = ["".join(row) for row in board]
sys.stdout.write("\n".join(board))
