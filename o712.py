from itertools import cycle
right_turn = cycle(((0,1),(1,0),(0,-1),(-1,0))).__next__
M,N,k,r,c = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(M)]
score = 0
i,j = r,c
count = 0
dy,dx = right_turn()
while 1:
    if nums[i][j] == 0:
        break
    score += nums[i][j]
    nums[i][j] -= 1
    count += 1
    if score % k == 0:
        dy,dx = right_turn()
    while 1:
        if (i == M-1 and dy == 1) or (j == N-1 and dx == 1) or (i == 0 and dy == -1) or (j == 0 and dx == -1) or nums[i+dy][j+dx] == -1:
            dy,dx = right_turn()
        else:
            break
    i += dy
    j += dx
print(count)
    

