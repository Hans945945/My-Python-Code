import sys
data = sys.stdin.read().splitlines()[:-1]
output = []
for s in data:
    r = f'"{s.strip()}"'if s.isalpha() else s.strip()
    output.append(f'print({r})')
sys.stdout.write("\n".join(output) + "\n")
