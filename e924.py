T = int(input())
pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

for _ in range(T):
    words = input()
    stack = []
    valid = True
    
    for char in words:
        if char in pairs:  # 左括號
            stack.append(char)
        elif char in pairs.values():  # 右括號
            if not stack or pairs[stack.pop()] != char:
                valid = False
                break
    
    # 檢查堆疊是否為空
    if valid and not stack:
        print("Y")
    else:
        print("N")
