from itertools import accumulate
import operator
d = ({'ONE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5,
      'SIX': 6, 'SEVEN': 7, 'EIGHT': 8, 'NINE': 9, 'TEN': 10,
      'ELEVEN': 11, 'TWELVE': 12, 'THIRTEEN': 13})
nums = []
objects = []
for _ in range(4):
    data = input().split()
    nums.append(d[data[3]])
    objects.append(data[4])
index = input().split()[2].rstrip("?")
nums = list(accumulate(nums, operator.mul))
print(nums[objects.index(index)], index)

    
