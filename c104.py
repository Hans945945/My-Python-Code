import sys
def is_safe(row, col, queens):
    for r, c in enumerate(queens):
        if c == col or abs(row-r) == abs(c-col):
            return 0
    return 1

def dfs(row, queens, board, Sum):
    if row == 8:
        return Sum
    max_sum = 0
    for c in range(8):
        if is_safe(row,c,queens):
            queens.append(c)
            max_sum = max(max_sum, dfs(row+1, queens, board, Sum + board[row][c]))
            queens.pop()
    return max_sum

data = sys.stdin.readlines()
T = int(data.pop(0))
for i in range(T):
    board = [list(map(int, data[8*i+j].split())) for j in range(8)]
    print(f"{dfs(0, [], board, 0):>5}")
    
