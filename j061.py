import sys
case = 1
while True:
    n = int(input())
    if n == 0:
        break
    sys.stdout.write(f"Case {case}:\n")
    sys.stdout.write("#include<string.h>\n")
    sys.stdout.write("#include<stdio.h>\n")
    sys.stdout.write("int main()\n")
    sys.stdout.write("{\n")
    for _ in range(n):
        r = ""
        for w in input():
            if w == '"':
                r += '\\"'
            elif w == "\\":
                r += "\\\\"
            else:
                r += w
        sys.stdout.write(f'printf("{r}\\n");\n')
    sys.stdout.write('printf("\\n");\n')
    sys.stdout.write('return 0;\n')
    sys.stdout.write("}\n")
    case += 1
