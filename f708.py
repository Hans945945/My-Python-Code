import sys
n,m = map(int, sys.stdin.readline().split())
if n <= m:
    print("No")
    sys.stdin.readline()
    sys.stdin.readline()
else:
    ants_h = sum(map(int, sys.stdin.readline().split()))
    grasshoppers_h = sum(map(int, sys.stdin.readline().split()))
    print("Yes" if ants_h > grasshoppers_h else "No")
