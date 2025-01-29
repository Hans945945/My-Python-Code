T = int(input())
for i in range(1,T+1):
    grades = list(map(int, input().split()))
    worst = min(grades[4:7])
    grade = sum(grades[:4])+(sum(grades[4:7])-worst)/2
    if grade >= 90:
        level = "A"
    elif grade >= 80:
        level = "B"
    elif grade >= 70:
        level = "C"
    elif grade >= 60:
        level = "D"
    else:
        level = "F"
    print(f"Case {i}: {level}")
    
