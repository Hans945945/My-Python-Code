import sys
holes = {"8": 2, "0": 1, "6": 1, "9": 1}
sys.stdout.write("\n".join(str(sum(holes.get(c, 0) for c in line.strip())) for line in sys.stdin) + "\n")
