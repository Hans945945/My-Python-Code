word = list(input())
DL = list("AHIMOTUVWXY")
designated_letters_only = (word == [i for i in word if i in DL])
original = word.copy()
word.reverse()
if word == original and designated_letters_only:
    print("Yes")
else:
    print("No")
