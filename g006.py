from collections import Counter
code = input()
change = Counter(code)
print("".join(key for time,key in sorted((-time,key) for key, time in change.items())))
