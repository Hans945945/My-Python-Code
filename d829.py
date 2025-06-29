import sys
for s in sys.stdin.readlines()[:-1]:
    s = list(s.rstrip())
    n = len(s)

    i = n - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1

    if i == -1:
        print("No Successor")
        continue

    j = n - 1
    while s[j] <= s[i]:
        j -= 1

    s[i], s[j] = s[j], s[i]
    s[i + 1:] = s[i + 1:][::-1]
    print("".join(s))
