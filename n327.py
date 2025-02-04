import sys
n = int(sys.stdin.readline())
names = sys.stdin.readlines()
names.sort(key=lambda name: (len(name), name))
sys.stdout.write("\n".join(names)+"\n")
