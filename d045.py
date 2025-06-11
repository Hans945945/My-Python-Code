T = int(input())

for case in range(1, T + 1):
    solved = []

    for _ in range(3):
        temp = list(map(int, input().split()))
        solved.append(set(temp[1:]))
        
    unique = [sorted(solved[i] - (solved[(i + 1) % 3] | solved[(i + 2) % 3])) for i in range(3)]
    max_len = max(len(uniq) for uniq in unique)

    print(f"Case #{case}:")
    for i in range(3):
        if len(unique[i]) == max_len:
            print(f"{i + 1} {len(unique[i])}", *unique[i])
