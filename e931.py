a = int(input())
b = int(input())

ans = a * b
width = len(str(ans))

steps = []
for i, d in enumerate(reversed(str(b))):
    part = a * int(d)
    steps.append(str(part) + ' ' * i)

print(f"{a:>{width}}")
print(f"{b:>{width}}")
print('-' * width)
for s in steps:
    print(f"{s:>{width}}")
if len(steps) > 1:
    print('-' * width)
    print(f"{ans:>{width}}")
