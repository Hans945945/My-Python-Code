import sys
t, n = sys.stdin.readline().split()
t = t.replace(n, "")
print("Yes" if t == t[::-1] else "No")
