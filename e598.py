n = int(input())
flag = 1
for i in range(2,8):
    if n % i == 0 and n//i > 99999999:
        flag = 0
        break
print("yes" if flag else "no")
