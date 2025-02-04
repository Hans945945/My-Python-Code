import sys
words = sys.stdin.readline().strip()
sys.stdout.write(words.replace(" ", f" {sys.stdin.readline().strip()} ")+"\n")
