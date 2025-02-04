import sys
sys.stdout.write("\n".join("".join(chars) for chars in zip(*sys.stdin.read().splitlines())) + "\n")
