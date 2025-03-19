import sys
r = []
stack = []
for s in sys.stdin.readlines()[1:]:
    data = s.split()
    if len(data) == 1:
        if data[0] == "1":
            stack.pop()
        else:
            r.append(stack[-1])
    else:
        stack.append(data[1])
sys.stdout.write("\n".join(r)+"\n") 
