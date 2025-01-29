T = int(input())
for _ in range(T):
    n = int(input())
    instructions = []
    for _ in range(n):
        temp = input().split()
        if temp[0] != "SAME":
            if temp[0] == "LEFT":
                instructions.append(-1)
            else:
                instructions.append(1)
        else:
             instructions.append(instructions[int(temp[2])-1])
    print(sum(instructions))
                
