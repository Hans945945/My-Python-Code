import sys
import itertools

words = []
for i in range(1, 6):
    for combination in itertools.combinations("abcdefghijklmnopqrstuvwxyz", i):
        words.append("".join(combination))

table = {word: index + 1 for index, word in enumerate(words)}

sys.stdout.write("\n".join(map(str, [table.get(s.strip(), 0) for s in sys.stdin.readlines()]))+"\n")

