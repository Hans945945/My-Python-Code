import sys
sys.stdout.write("\n".join(str(sum(map(int, s.split()))) for s in sys.stdin.readlines()[1:])+"\n")
    
