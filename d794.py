import bisect
while True:
    try:
        n = int(input())
        grades = []
        for i in range(n):
            grade = int(input())
            pos = bisect.bisect_left(grades, grade)
            grades.insert(pos, grade)
            print(i - pos +1)
    except EOFError:
        break
