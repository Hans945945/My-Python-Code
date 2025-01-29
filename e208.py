import sys
data = sys.stdin.read().splitlines()
case = 0
r = []
for s in data[1:]:
    case += 1
    words = []
    nums = []
    n = []
    for w in s.strip():
        if w.isalpha():
            words.append(w)
            if n:
                nums.append(int(''.join(n)))
                n = []
        else:
            n.append(w)
    nums.append(int(''.join(n)))
    string = list(zip(words, nums))
    r.append(f"Case {case}: {''.join(w*num for w, num in string)}")
sys.stdout.write("\n".join(r)+"\n")
