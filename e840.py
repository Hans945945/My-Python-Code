password = input()
n = len(password)
score = 3*n
last = 0 #is last chr a number
nums = []
for p in password:
    if p.isdigit():
        nums.append(p)
        if last:
            score -= 2
        last = 1
    else:
        last = 0
num_len = len(nums)
if  num_len == n:
    score -= n+5
elif not nums:
    score -= n+5
elif n < 8:
    score -= 5
else:
    score += 10
score += num_len*2
score += (n-num_len)*3
print(score)




