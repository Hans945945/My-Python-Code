nums = list(map(int, input().split()))
ans = nums.pop()
a = b = c = d = e = nums.pop(0)
for n in nums:
    a += n
    b -= n
    c *= n
    d //= n
    e **= n
if a == ans:
    print("+")
if b == ans:
    print("-")
if c == ans:
    print("*")
if d == ans:
    print("/")
if e == ans:
    print("**")
