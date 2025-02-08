import sys
title = sys.stdin.readline().strip().split()
r = []
special = ["the", "a", "an", "in", "on", "at", "of", "for", "by", "to", "and", "or", "but"]
for word in title:
    if word.lower() not in special or not r or len(r)== len(title)-1:
        r.append(word.title())
    else:
        r.append(word.lower())
sys.stdout.write(" ".join(r)+"\n")
        
