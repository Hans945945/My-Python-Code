n = int(input())
nums = list(map(int, input().split()))
left = [n for n in nums if n%2 == 1]
right = [n for n in nums if n%2 == 0]
right.sort()
left.sort(reverse = True)
print(" ".join(map(str, right+left)))
