import sys
from collections import Counter
data = sys.stdin.readlines()
rule = data[0].strip()
words = data[1].strip()
table = Counter(words)
r = []
for w in rule:
    r.append(w*table[w])
words = "".join(r)
sys.stdout.write("\n".join(words[int(n)-1] for n in data[3:])+"\n")
