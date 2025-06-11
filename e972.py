import sys
rates = {
    'T': 1.0,
    'U': 30.9,
    'J': 0.28,
    'E': 34.5
}
data = sys.stdin.read().replace('\r', '\n').split('\n')
n = int(data[0])
m, c = data[1].split()
m = int(m)

now = n / rates[c] - m
if now< 0:
    print("No Money")
else:
    if 0 < now < 0.05:
        now = 0.00
    print(f"{c} {now:.2f}")
