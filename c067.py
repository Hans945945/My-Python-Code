n = int(input())
k = 0
while n != 0:
    k+=1
    print(f'Set #{k}')
    bricks = list(map(int, input().split()))
    a = sum(bricks)//n
    bricks.sort(reverse= True)
    move = 0
    for i in range(n):
        if bricks[i] <= a:
            break
        else:
            move += bricks[i]-a
            print(f'The minimum number of moves is {move}.')
            print()
    n = int(input())
