import sys
sys.stdout.write("\n".join("LOOP "if s.count("M") == s.count("F") and len(s.split())>1 else "NO LOOP" for s in sys.stdin.readlines()[1:])+"\n")
  
