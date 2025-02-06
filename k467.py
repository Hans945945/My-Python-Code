import sys
lines = sys.stdin.readlines()
n = int(lines[0])
chinese_grades = list(map(int, lines[1].split()))
math_grades = list(map(int, lines[2].split()))
chinese_class = []
math_class = []
for i in range(n):
    if chinese_grades[i] > math_grades[i]:
        chinese_class.append(i+1)
    else:
        math_class.append(i+1)
sys.stdout.write(" ".join(map(str,chinese_class))+"\n" if chinese_class else "-1\n")
sys.stdout.write(" ".join(map(str,math_class))+"\n" if math_class else "-1\n")
