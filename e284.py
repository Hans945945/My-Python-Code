import sys
table = [1]*32
for i in range(1,32):
    table[i] = table[i-1] *2
table = set(table)
sys.stdout.write("\n".join("Yes" if int(s) in table else "No" for s in sys.stdin.readlines())+"\n")
