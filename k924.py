import sys
n = sys.stdin.read().replace(" ", "").strip()
print("Yes" if int(n) % 11 == 0 else "No")
