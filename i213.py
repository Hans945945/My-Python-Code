stack = []
def push(data):
    stack.append(data)
def size():
    print(len(stack))
def pop():
    r = stack.pop()
    return r
def top():
    now = len(stack)
    t = stack[now-1]
    return t
def empty():
    if len(stack) == 0:
        return True
    else:
        return False
for k in range(int(input())):
    a = input().split()
    t = a[0]
    if t == "1":
        push(a[1])
    elif t == "2":
        if not empty():
            print(top())
        else:
            print(-1)
    elif t == "3":
        if not empty():
            pop()
