import sys
sys.stdout.write("\n".join("YES" if "!" in s else "NO" for s in sys.stdin.readlines())+"\n")
