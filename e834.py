import sys
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))[:-1]
sys.stdout.write("\n".join(str(n // m if n % m == 0 else m - n % m) for n in nums) + "\n")
