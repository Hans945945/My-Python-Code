from collections import Counter
import sys
input()
women = []
for s in sys.stdin:
    women.append(s.split()[0])
result = sorted(set(women))
numbers = Counter(women)
for r in result:
    print(r, numbers[r])
