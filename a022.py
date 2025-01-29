word = input()
new_word = ""
words = [i for i in word]
words.reverse()
for j in words:
    new_word = new_word+j
if new_word == word:
    print("yes")
else:
    print("no")
