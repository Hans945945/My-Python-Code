nums = input().split()
r = []
for n in nums:
    if n == "+":
        r.append(r.pop()+r.pop())
    elif n == "-":
        a = r.pop()
        b = r.pop()
        r.append(b-a)
    elif n == "*":
        r.append(r.pop()*r.pop())
    elif n == "/":
        a = r.pop()
        b = r.pop()
        r.append(b//a)
    else:
        r.append(int(n))
print(r.pop())
