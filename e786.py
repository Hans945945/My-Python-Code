s = input()
if s == s[::-1] and len(s) % 2 == 0:
    print("YES")
    print(s[:len(s)//2])
else:
    print("NO")
