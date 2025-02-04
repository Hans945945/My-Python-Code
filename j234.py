import sys
n,m = map(int, sys.stdin.readline().split())
first = set(sys.stdin.readline().split())
second = set(sys.stdin.readline().split())
print(len(first-second))
