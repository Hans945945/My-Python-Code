import sys
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
input()
for s in sys.stdin:
    m, d = map(int, s.split())
    d += sum(month[:m])
    print(week[d%7])
