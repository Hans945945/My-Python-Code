import random
import sys
import string

w,v1,v2 = map(int, input().split())
seen = set()
r = []
for i in range(v1,v2+1):
    word = "".join(random.choices(string.ascii_lowercase, k=i))
    if word not in seen:
        seen.add(word)
        word = word.title()
        r.append(f"{word}: hello, {word}")
        w -= 1
while w > 0:
    word = "".join(random.choices(string.ascii_lowercase, k=random.randint(v1,v2)))
    if word not in seen:
        seen.add(word)
        word = word.title()
        r.append(f"{word}: hello, {word}")
        w -= 1
sys.stdout.write("\n".join(r)+"\n")

    
    
