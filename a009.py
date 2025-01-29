words = list(input())
new_words = []

K = 7

for i in words:
    new_words.append(chr(ord(i)-K))
print("".join(new_words))
