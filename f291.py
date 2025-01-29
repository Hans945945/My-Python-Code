a = input()
words = [l for l in a if l.isalpha()]
nums = [l for l in a if not l.isalpha()]
y = int("".join(nums))
x = 0
for i in range(len(words)):
    x += (ord(words[i])-64)*26**(len(words)-i-1)
print(x*y)
        
