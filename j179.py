n = input()

while len(n) != 1:
    l = len(n)
    if l == 4:
        left, right = str(int(n[:2])), str(int(n[2:]))
        left = str(int(left[0]) * int(left[1])) if len(left) == 2 else left
        right = str(int(right[0]) * int(right[1])) if len(right) == 2 else right
        n = str(int(left + right))
    elif l == 3:
        n = str(int(n[0]) * int(n[1])) + str(int(n[2]) * int(n[1]))
    elif l == 2:
        n = str(int(n[0]) * int(n[1]))

print(n)

