import sys
for s in sys.stdin:
    sys.stdout.write("konopad!\n" if int(s)%81 == 0 else "konosuba!\n")
