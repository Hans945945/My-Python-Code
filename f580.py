data = input().split()
n = int(data[0])
m = int(data[1])
dice = []
for _ in range(n):
    dice.append(1)
    dice.append(3)
    dice.append(5)
print(dice)
for _ in range(m):
    nums = input().split()
    a = int(nums[0])-1
    b = int(nums[1])
    if a>=0 and b>=0:
        for i in range(3):
            temp = dice[a*3]
            dice[a*3] = dice[(b-1)*3]
            dice[(b-1)*3] = temp
    elif b == -1:
        temp = dice[a*3]
        dice[a*3] = dice[a*3+1]
        dice[a*3+1] = 7-temp
    elif b == -2:
        temp = dice[a*3]
        dice[a*3] = dice[a*3+2]
        dice[a*3+2] = 7-temp
for i in range(n):
    print(dice[i*3],end = " ")
