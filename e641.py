table = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0, 'H': 0, 'W': 0, 'Y': 0, 'B': 1, 'F': 1, 'P': 1, 'V': 1, 'C': 2, 'G': 2, 'J': 2, 'K': 2, 'Q': 2, 'S': 2, 'X': 2, 'Z': 2, 'D': 3, 'T': 3, 'L': 4, 'M': 5, 'N': 5, 'R': 6}         
while True:
    try:
        word = input()
        last = None
        r = ""
        for w in word:
            now = table[w]
            if now != 0:
                if now != last:
                    r+=str(now)
                last = now
            else:
                last = None
        print(r)
    except EOFError:
        break
