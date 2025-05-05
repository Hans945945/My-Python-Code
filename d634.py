import sys
r = [s for s in sys.stdin.readlines()[1:]]
r.sort()
sys.stdout.write("\n".join(r)+"\n")
