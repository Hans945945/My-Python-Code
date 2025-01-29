import sys
for s in sys.stdin:
    words = s
    count = 0
    last = 1 #1 if words 0 if not
    for w in words:
        if not(ord(w) > 64 and ord(w) <= 90) and not(ord(w) > 96 and ord(w) <= 122):
            if last:
                count += 1
                last = 0
        else:
            last = 1
    print(count)
