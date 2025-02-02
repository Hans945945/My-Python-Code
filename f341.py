import sys
s = sys.stdin.readline().strip()
a,m,b = s.partition(sys.stdin.readline().strip())
sys.stdout.write(f"{b[::-1]}{m}{a[::-1]}\n")
