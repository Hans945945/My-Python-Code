import sys
def check(n,a):
    count = 0
    last = False
    for w in a:
        if w in "aeiouy":
            if not last:
               count += 1
            last = True
        else:
            last = False
    return count == n

r = []
for s in sys.stdin.readlines()[:-1]:
    lines = s.rstrip().split("/")
    expected_syllables = [5, 7, 5]

    for i in range(3):
        if not check(expected_syllables[i], lines[i]):
            r.append(f"{i+1}")
            break
    else:
        r.append("Y")
sys.stdout.write("\n".join(r)+"\n")
            
                               
