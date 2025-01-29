from collections import Counter
n = int(input())
while n != 0:
    students = []
    for i in range(n):
        s = ''.join(sorted(input().split()))
        students.append(s)
    s2 = Counter(students)
    m= max(s2.values())
    count = sum(1 for x in s2.values() if x == m)
    print(m *count)
    n = int(input())
    
        
