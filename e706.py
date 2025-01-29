from collections import Counter
case = 1
while True:
    try:
        n = int(input())
        count = 0
        for _ in range(n):
            f = Counter(input()).values()
            if len(f) == len(set(f)) and len(f) != 1:count += 1 
        print(f"Case {case}: {count}")
        case += 1
    except EOFError:
        break
    
    
