import sys

R2I = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

I2R = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'),  (90, 'XC'), (50, 'L'),  (40, 'XL'),
    (10, 'X'),   (9, 'IX'),  (5, 'V'),   (4, 'IV'),
    (1, 'I')
]

def RtoI(s):
    total = 0
    last = 0
    for w in s[::-1]:
        v = R2I[w]
        total += v if v >= last else -v
        last = v
    return total

for s in sys.stdin.readlines()[:-1]:
    a, b = s.split()
    diff = abs(RtoI(a) - RtoI(b))

    if diff == 0:
        print("ZERO")
    else:
        r = ""
        for v, w in I2R:
            while diff >= v:
                r += w
                diff -= v
        print(r)
