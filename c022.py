T = int(input())
for j in range(T):
    a = int(input())
    b = int(input())
    if a %2 == 1:
        print(f"Case {j+1}: {sum([i for i in range(a,b+1,2)])}")
    else:
        print(f"Case {j+1}: {sum([i for i in range(a+1,b+1,2)])}")
