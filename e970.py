import sys
n = int(sys.stdin.readline())
comments = list(map(int, sys.stdin.readline().split()))
base = comments[-1]
m = sum(comments[i-1] for i in range(1, n+1, base))%n
if m == 0:
    m = n
lucky = comments[m-1]
sys.stdout.write(f"{m} {lucky}\n")
