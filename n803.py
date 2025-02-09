import sys
sys.stdout.write("\n".join(str(int(n)//2) for n in sys.stdin.readlines()[:-1])+"\n")
    
