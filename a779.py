import sys
for s in sys.stdin:
    inputs = s.replace("\n","")
    print(inputs)
    sentence = [char.lower() for char in inputs if char.isalnum()]
    old = sentence.copy()
    sentence.reverse()
    new = sentence
    if old == new:
        print("-- is a palindrome")
    else:
        print("-- is not a palindrome")
