import sys
n = int(input())
grades = []
for s in sys.stdin:
    num, c_grade, m_grade, e_grade = map(int, s.split())
    avg = (c_grade*5+m_grade*3+e_grade*2)/10
    if avg == int(avg):
        avg = int(avg)
    grades.append((avg, c_grade, m_grade, e_grade, -num))
    grades.sort(reverse = True)
    r = [f"{-num} {avg}" for avg, g1, g2, g3, num in grades]
sys.stdout.write("\n".join(r)+"\n")
