T = int(input())
weekdays = {"SUN": 7, "MON": 6, "TUE": 5, "WED": 4, "THU": 3, "FRI": 2, "SAT": 1}
months = {
    "JAN": 31, "FEB": 28, "MAR": 31, "APR": 30,
    "MAY": 31, "JUN": 30, "JUL": 31, "AUG": 31,
    "SEP": 30, "OCT": 31, "NOV": 30, "DEC": 31
}

for _ in range(T):
    c,d = input().split()
    a, b = weekdays[d], months[c]
    b -= a
    ans = (a >= 2) + (a >= 1) + (b // 7) * 2 + int(b % 7 == 6)
    print(ans)
