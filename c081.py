import sys
from itertools import permutations

colors = ['B', 'C', 'G']
for s in sys.stdin:
    nums = list(map(int, s.strip().split()))
    min_moves = float('inf')
    r = ''
    total = sum(nums)
    
    for order in list(permutations(colors)):
        keep = 0
        for i, color in enumerate(order):
            idx = i * 3  
            if color == 'B':
                keep += nums[idx]
            elif color == 'G':
                keep += nums[idx + 1]
            elif color == 'C':
                keep += nums[idx + 2]
        moves = total - keep
        if moves < min_moves:
            min_moves = moves
            r = ''.join(order)
    print(f"{r} {min_moves}")
