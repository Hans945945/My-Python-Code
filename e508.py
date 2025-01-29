T = int(input())
for i in range(T):
    n = int(input())
    subjects = []
    days = []
    for _ in range(n):
        sub, d = input().split()
        subjects.append(sub)
        days.append(int(d))
    D = int(input())
    homework = input()
    if subjects.count(homework) == 0:
        print(f"Case {i+1}: Do your own homework!")
    else:
        need = days[subjects.index(homework)]
        if need <= D:
            print(f"Case {i+1}: Yesss")
        elif need <= D+5:
            print(f"Case {i+1}: Late")
        else:
            print(f"Case {i+1}: Do your own homework!")
