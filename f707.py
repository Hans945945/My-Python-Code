import sys
nums = list(map(int, sys.stdin.readline().split()))[:-1]
biggest = [n for n in nums if n % 7 == 0]
if biggest:
    if len(biggest) == 1:
        print(biggest[0])
    else:
        max_remainder = 0
        winner = 0
        for b in biggest:
            if b % 70 > max_remainder:
                max_remainder = b%70
                winner = b
        print(winner)
else:
    min_remainder = float("inf")
    winner = 0
    for n in nums:
        if n % 77 < min_remainder:
            min_remainder = n%77
            winner = n
    print(winner)
