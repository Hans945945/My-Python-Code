import sys
def find(n):
    if n % 6 == 0:
        return "1"
    if n % 3 != 0 and int(str(n)[-1]) % 2 == 1:
        return "2"
    if n**0.5 == int(n**0.5) or (n%7!= 0 and n%2 == 0):
        return "3"
    return "0"
n = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
r = [find(p) for p in people]
sys.stdout.write(" ".join(r)+"\n")
