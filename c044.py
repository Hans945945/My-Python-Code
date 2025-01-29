import sys
from collections import Counter
n = int(input())
wordbank = []
for s in sys.stdin:
    words = s.strip().replace(" ", "")
    words = [w.upper() for w in words if w.isalpha()]
    wordbank.append("".join(words))
word = Counter("".join(wordbank))
count = [(-value, key) for key, value in word.items()]
count.sort()
count = [f"{key} {-value}" for value, key in count]
sys.stdout.write("\n".join(count))
