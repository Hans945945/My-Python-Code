import sys
from collections import Counter
words = Counter(sys.stdin.readline())
result = []
for key, value in sorted(words.items()):
    result.append(key * value)
sys.stdout.write("".join(result) + "\n")
